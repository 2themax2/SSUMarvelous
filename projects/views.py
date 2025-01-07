from .models import RoleTest, Student
from rest_framework import serializers, viewsets
from rest_framework.response import Response

# Serializers define the API representation.
class RoleTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleTest
        fields = ['role', 'question']

# ViewSets define the view behavior.
class RoleTestViewSet(viewsets.ModelViewSet):
    queryset = RoleTest.objects.all()
    serializer_class = RoleTestSerializer

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'plant', 'investigator', 'coordinator', 'shaper', 'monitor', 'teamworker', 'implementer', 'C', 'specialist']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        scores = request.data.get()
        student = Student.objects.get(student_nr=440536)
        student.plant = scores[0] + scores[1]
        student.investigator = scores[2] + scores[3]
        student.coordinator = scores[4] + scores[5]
        student.shaper = scores[6] + scores[7]
        student.monitor = scores[8] + scores[9]
        student.teamworker = scores[10] + scores[11]
        student.implementer = scores[12] + scores[13]
        student.specialist = scores[14] + scores[15]
        student.specialist = scores[16] + scores[17]
        student.save()        
        return Response(serializer.data)