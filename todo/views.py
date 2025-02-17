from rest_framework import mixins 
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render

from todo.models import Todo
from todo.serializers import TodoSerialzier

# Create your views here.

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerialzier
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Todo.objects.filter(user_id=user_id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerialzier
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Todo.objects.filter(user_id=user_id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}    
    
            
