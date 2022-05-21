from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #homepage
    path('learning_logs/', views.index, name= 'index'),
    # Page that shows all topics.
    path('learning_logs/topics/', views.topics, name= 'topics'),
    # Detail page for a single topic.
    path('learning_logs/topics/<int:topic_id>/', views.topic, name= 'topic'),
    # Page for adding a new topic
    path('learning_logs/topics/new_topic/', views.new_topic, name= 'new_topic'),
    # Page for adding a new entry
    path('learning_logs/topics/<int:topic_id>/new_entry/', views.new_entry, name= 'new_entry'),
    # page for editing an entry
    path('learning_logs/topics/topic/edit_entry/<int:entry_id>/', views.edit_entry, name= 'edit_entry'),
    # path('learning_logs/testing/', views.testing, name='testing')
]