"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    # Сторінка з темами
    path('topics/', views.topics, name='topics'),
    # Сторінка одної теми
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Сторінка для додавання однієї теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # Сторінка для додавання нового допису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Сторінка для редагування допису
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
