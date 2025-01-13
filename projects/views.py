from rest_framework.decorators import action

from .models import RoleTest, Student
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .serializers import RoleTestSerializer, StudentSerializer
from collections import Counter

# Serializers define the API representation.

from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})

# ViewSets define the view behavior.
class RoleTestViewSet(viewsets.ModelViewSet):
    queryset = RoleTest.objects.all()
    serializer_class = RoleTestSerializer


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
    
    @action(detail=False, methods=['get'])
    def get_test_result(self, request, student_nr=None):
        if not student_nr:
            return Response({"error": "Must give a student number: student/{student_nr}/get_test_result"}, status=400)
        student = Student.objects.get(student_nr=student_nr)
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

        return Response([scores, top_three], status=200)