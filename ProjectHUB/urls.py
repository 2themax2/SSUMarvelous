# back/urls.py
from django.contrib import admin
from django.urls import path, include
from ProjectHUB.projects import urls as projects_urls
from projects.views import get_csrf_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(projects_urls)),
]