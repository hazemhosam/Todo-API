from rest_framework import serializers

from todo.models import Todo 

class TodoSerialzier(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Todo 
        fields = ['id','user_id','title','description','completed','created_at']

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Todo.objects.create(user_id=user_id,**validated_data)
    


        
        