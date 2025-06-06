from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    es_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Cambia a un nombre único
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_permission_user_set",  # Cambia a un nombre único
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    ) 
    
    def __str__(self):
        return self.username