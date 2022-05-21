"""Defines URL patterns for repositories"""

from django.urls import path
from . import views

app_name = 'repositories'
urlpatterns = [
    # include url that produces the repositories page
    path('repositories/',  views.repositories, name='index'),
    path('repositories/new_repository/', views.new_repository, name= 'new_repository')
]
