from rest_framework.viewsets import ModelViewSet
from .serializers import UsuarioResponseSerializer, UsuarioCrearSerializer
from .models import User

class UsuarioViewset(ModelViewSet):

    serializer_class=UsuarioResponseSerializer
    queryset= User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCrearSerializer
        return UsuarioResponseSerializer