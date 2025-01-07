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
        fields = ['first_name', 'last_name', 'plant', 'investigator', 'coordinator', 'shaper', 'monitor', 'teamworker', 'implementer', 'finisher', 'specialist']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        scores = request.data.get()
        return Response(serializer.data)