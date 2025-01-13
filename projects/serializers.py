from rest_framework import serializers
from .models import Project, RoleTest, Student

# Serializers define the API representation.
class RoleTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleTest
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'