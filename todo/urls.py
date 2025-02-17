from django.urls import include, path 
from . import views

urlpatterns = [
    path('tasks/',views.TodoList.as_view()),
    path('tasks/<int:pk>/',views.TodoDetail.as_view())
]