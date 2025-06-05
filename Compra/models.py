from django.db import models
from usuario.models import User
from categoriaProducto.models import Producto
from datetime import date
# Create your models here.
class Compra(models.Model):
    producto=models.ForeignKey(Producto,related_name='compra_producto',on_delete=models.SET_NULL,blank=True,null=True)
    usuario=models.ForeignKey(User,related_name='compra_usuario',on_delete=models.SET_NULL, blank=True, null=True)
    cantidad=models.IntegerField()
    fecha=models.DateField(default=date.today())

    def __str__(self):
        return self.id
    

    