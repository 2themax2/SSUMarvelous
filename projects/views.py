from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Project, ProjectStudents, RoleTest, Student, Role, Teacher
from .serializers import ProjectSerializer, RoleTestSerializer, StudentSerializer, RoleSerializer
from collections import Counter

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

# ViewSets define the view behavior.
class RoleTestViewSet(viewsets.ModelViewSet):
    queryset = RoleTest.objects.all()
    serializer_class = RoleTestSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['post'])
    def calculate_scores(self, request):
        scores = request.data.get('answers')  # Zorg ervoor dat je een lijst 'scores' in je request meestuurt
        if not scores or len(scores) < 18:
            return Response({"error": "Scores must have at least 18 values"}, status=400)

        student = Student.objects.get(student_nr=440536)
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
            "plant" : student.plant,
            "investigator" : student.investigator,
            "coordinator" : student.coordinator,
            "shaper" : student.shaper,
            "monitor" : student.monitor,
            "teamworker" : student.teamworker,
            "implementer" : student.implementer,
            "finisher" : student.finisher,
            "specialist" : student.specialist,
        }

        scores_counter = Counter(scores)
        top_three = scores_counter.most_common(3)
        student.role = top_three[0][0]
        student.save()

        return Response([scores, top_three], status=200)
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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