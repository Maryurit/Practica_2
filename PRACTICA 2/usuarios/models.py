from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, blank=True, verbose_name="Dirección")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    def __str__(self):
        return self.username  # o `self.nombre` si prefieres
    
    pass
