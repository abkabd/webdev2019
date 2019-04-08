from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('task_lists/', views.getAllTasksList),
    path('task_lists/<int:pk>/', views.getOneTaskList),
    path('task_lists/<int:pk>/tasks/', views.getTaskByTaskListID),

]
