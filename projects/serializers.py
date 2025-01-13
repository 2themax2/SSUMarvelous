from rest_framework import routers,serializers,viewsets
from .models import RoleTest, Student


class RoleTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleTest
        fields = ['role', 'question']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'plant', 'investigator', 'coordinator', 'shaper', 'monitor', 'teamworker', 'implementer', 'finisher', 'specialist']


