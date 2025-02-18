from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import DefaultPagination
from todo.models import Todo
from todo.serializers import TodoSerialzier

# Create your views here.

class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerialzier
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['completed']  
    search_fields = ['title','description']
    pagination_class = DefaultPagination

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
    
            
