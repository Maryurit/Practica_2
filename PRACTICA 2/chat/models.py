from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    es_privada = models.BooleanField(default=False)
    participantes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='salas')
    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='mensajes')
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente.username} en {self.sala.nombre}: {self.contenido[:20]}...'
