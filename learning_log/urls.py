"""Defines URL patterns for the entire learning_log project(i.e include set of URLs
for different apps used in the project"""
from django.contrib import admin
from django.urls import path, include
from .homeview import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    path('', home_page),
    # path('', include('wedia.urls')),
    path('/learning logs', include('learning_logs.urls')),
    path('/repositories', include('repositories.urls')),
    # path('', include('files_app.urls')),
    # path('accounts/', include('allauth.urls'))
    ]