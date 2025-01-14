from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Project, ProjectStudents, RoleTest, Student, Role, Teacher
from .serializers import ProjectSerializer, RoleTestSerializer, StudentSerializer, RoleSerializer, TeacherSerializer
from collections import Counter
import math


def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})


# ViewSets define the view behavior.
class RoleTestViewSet(viewsets.ModelViewSet):
    queryset = RoleTest.objects.all()
    serializer_class = RoleTestSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['post'])
    def calculate_scores(self, request):
        scores = request.data.get('answers')  # Zorg ervoor dat je een lijst 'scores' in je request meestuurt
        student_data = request.data.get('student') # Bevat: student_nr (len 6), first_name (max_len 30), last_name (max_len 30), mayor (max_len 80)
        if not scores or len(scores) < 18:
            return Response({"error": "Scores must have at least 18 values"}, status=400)
        try:
            student = Student.objects.get(student_nr=student_data['student_nr'])
        except:
            student = Student.objects.create(student_nr=student_data['student_nr'], first_name=student_data['first_name'], last_name=student_data['last_name'], mayor=student_data['mayor'])
        student.plant = scores[0] + scores[1]
        student.investigator = scores[2] + scores[3]
        student.coordinator = scores[4] + scores[5]
        student.shaper = scores[6] + scores[7]
        student.monitor = scores[8] + scores[9]
        student.teamworker = scores[10] + scores[11]
        student.implementer = scores[12] + scores[13]
        student.finisher = scores[14] + scores[15]
        student.specialist = scores[16] + scores[17]
        student.save()

        return Response("OK", status=200)

    @action(detail=True, methods=['get'])
    def get_test_result(self, request, pk=None):
        if not pk:
            return Response({"error": "Must give a student number: student/{student_nr}/get_test_result"}, status=400)
        student = Student.objects.get(student_nr=pk)
        if not student:
            return Response({"error": "Student not found."}, status=404)

        scores = {
            "plant": student.plant,
            "investigator": student.investigator,
            "coordinator": student.coordinator,
            "shaper": student.shaper,
            "monitor": student.monitor,
            "teamworker": student.teamworker,
            "implementer": student.implementer,
            "finisher": student.finisher,
            "specialist": student.specialist,
        }

        scores_counter = Counter(scores)
        top_three = scores_counter.most_common(3)
        student.role = top_three[0][0]
        student.save()

        return Response({'allScores': scores, 'topThree': top_three}, status=200)
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def get_all_projects(self, request):
        projects = Project.objects.all()
        projects_dict = {}
        for project in projects:
            projects_dict[project.project_nr] = {
                'project_nr' : project.project_nr,
                'name' : project.name,
                'description' : project.description,
                'teacher' : f"{project.teacher.first_name} {project.teacher.last_name}"
            }
        return Response(projects_dict, status=200)

    @action(detail=True, methods=['get'])
    def get_project(self, request, pk=None):
        if not pk:
            return Response({"error": "Must give a project number: project/{project_nr}/get_project"}, status=400)
        project = Project.objects.get(project_nr=pk)
        if not project:
            return Response({"error": "Project not found."}, status=404)

        nogroup = {}
        students = {}
        project_students = ProjectStudents.objects.filter(project__project_nr=1)
        count = 0
        for pr_st in project_students:
            student = Student.objects.get(id=pr_st.student.id)
            if pr_st.group_nr == None:
                nogroup[count] = {"name" : f"{student.first_name} {student.last_name}",
                            "mayor" : student.mayor,
                            "role" : student.role
                            }
                count += 1
            else:
                try:
                    students[pr_st.group_nr].append([{"name" : f"{student.first_name} {student.last_name}",
                        "mayor" : student.mayor,
                        "role" : student.role
                        }])
                except KeyError:
                    students[pr_st.group_nr] = [{"name" : f"{student.first_name} {student.last_name}",
                        "mayor" : student.mayor,
                        "role" : student.role
                        }]

        teacher = Teacher.objects.get(id=project.teacher.id)
        project_data= {
            "project_nr" : project.project_nr,
            "name" : project.name,
            "description" : project.description,
            "teacher" : f"{teacher.first_name} {teacher.last_name}",
            "students" : {
                "no_group" : nogroup,
                "groups" : students
                }
        }

        return Response(project_data, status=200)
    
    @action(detail=False, methods=['post'])
    def make_groups(self, request):
        project_nr = request.data.get('project_nr')
        students = ProjectStudents.objects.filter(project__project_nr=project_nr).order_by('student__role', 'student__mayor').values_list('student_id')
        project = Project.objects.get(project_nr=project_nr)
        if not project:
            return Response({"error": "Project not found."}, status=404)
        if len(students) == 0:
            return Response({"error": "No students in Project"}, status=404)
       
        total_st = len(students)
        if total_st % 5 == 4 or total_st % 5 == 0:
            groups = math.ceil(total_st / 5)
        else:
            groups = math.floor(total_st / 5)

        allocated = {}
        count = 1
        first = True
        for student_id in students:
            if first:
                allocated[count] = [student_id[0]]
            else:
                allocated[count] += [student_id[0]]
            if count < groups:
                count += 1
            else:
                count = 1
                first = False

        for key in allocated.keys():
            for value in allocated[key]:
                project_student = ProjectStudents.objects.get(student_id=value, project__project_nr=project_nr)
                project_student.group_nr = key
                project_student.save()

        return Response("OK", status=200)