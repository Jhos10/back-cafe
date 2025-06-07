from rest_framework.viewsets import ModelViewSet
from .serializers import CompraSerializer
from .models import Compra


class CompraViewset(ModelViewSet):
    serializer_class=CompraSerializer
    queryset=Compra.objects.all()

