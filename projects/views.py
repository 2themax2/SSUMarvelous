from .models import RoleTest, Student
from rest_framework import serializers, viewsets

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
    
    def update(self, request, *args, **kwargs):
        request.data.get()
        return super.update(request, *args, **kwargs)