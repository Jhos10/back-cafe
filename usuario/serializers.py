from rest_framework.serializers import ModelSerializer
from .models import User

class UsuarioResponseSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'email']

class UsuarioCrearSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'password', 'email']