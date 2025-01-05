# back/urls.py
from django.contrib import admin
from django.urls import path, include
from projects import urls as projects_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(projects_urls)),
]