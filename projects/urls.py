"""
URL configuration for ProjectHUB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from .views import csrf_token_view, RoleTestViewSet, StudentViewSet, ProjectViewSet, RoleViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register(r'roletest', RoleTestViewSet)
router.register(r'role', RoleViewSet)
router.register(r'student', StudentViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'teacher', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('csrf-token/', csrf_token_view, name='csrf-token'),
]