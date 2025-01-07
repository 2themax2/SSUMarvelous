from .models import RoleTest, Student
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.http import JsonResponse


#
# def get_csrf_token(request):
#     token = get_token(request)
#     return JsonResponse({'csrfToken': token})

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
    # @api_view(['GET','POST'])
    def create(self, request, *args, **kwargs):
        return Response({key: "value"})
        answers = request.data.get('answers', {})
        data = {
            'one': answers.get("one")
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # scores = request.data.get()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class TestSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         fields = ['answers']


# class TestViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # @api_view(['GET','POST'])
#     def create(self, request, *args, **kwargs):
#         return Response({key: "value"})
#         answers = request.data.get('answers', {})
#         data = {
#             'one': answers.get("one")
#         }
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         # scores = request.data.get()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)