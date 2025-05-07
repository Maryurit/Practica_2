from rest_framework import serializers
from .models import Sala, Mensaje
from usuarios.models import Usuario  # Tu modelo personalizado

class MensajeSerializer(serializers.ModelSerializer):
    remitente_username = serializers.CharField(source='remitente.username', read_only=True)

    class Meta:
        model = Mensaje
        fields = ['id', 'sala', 'remitente', 'remitente_username', 'contenido', 'timestamp']

class SalaSerializer(serializers.ModelSerializer):
    participantes = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.all())
    mensajes = MensajeSerializer(many=True, read_only=True)

    class Meta:
        model = Sala
        fields = ['id', 'nombre', 'es_privada', 'participantes', 'mensajes']
