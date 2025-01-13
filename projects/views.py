from rest_framework.decorators import action

from .models import RoleTest, Student
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .serializers import RoleTestSerializer, StudentSerializer
from django.views.decorators.csrf import csrf_exempt

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

        # scores = request.data.get()
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

        serializer = self.get_serializer(student)
        return Response(serializer.data)