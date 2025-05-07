from django.db import models
from django.conf import settings

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='eventos_imagenes/', blank=True, null=True)
    organizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
