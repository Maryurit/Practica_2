from django.db import models
from usuarios.models import Usuario  # Asumiendo que tu modelo personalizado está aquí

class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    comentario = models.TextField(blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.materia} - {self.nota}'
