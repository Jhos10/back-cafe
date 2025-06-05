from rest_framework.serializers import ModelSerializer
from .models import Producto,ProductoCategoria
class ProductoSerializer(ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'

class ProductoCategoriaSerializer(ModelSerializer):
    class Meta:
        model=ProductoCategoria
        fields='__all__'