from django.db import models

class ProductoCategoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precioUnidad = models.FloatField()
    categoria = models.ForeignKey(ProductoCategoria,related_name='categoria_producto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


