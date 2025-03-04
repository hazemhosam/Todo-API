from djoser.serializers import UserSerializer as BaseUserSerializer , UserCreateSerializer as BaseUserCreateSerializer


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','first_name','last_name',
                  'username', 'email', 'password']
        
class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','first_name','last_name',
                  'username', 'email']