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
# urls.py
from django.urls import include, path
from rest_framework import routers
from .views import RoleTestViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register(r'RoleTest', RoleTestViewSet)
router.register(r'Student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('csrf/', get_csrf_token, name='csrf_token'),
]