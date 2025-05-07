from rest_framework import serializers
from .models import Categoria, Respuesta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    autor_username = serializers.ReadOnlyField(source='autor.username')  # Para mostrar el nombre del autor

    class Meta:
        model = Respuesta
        fields = '__all__'
        read_only_fields = ['autor', 'fecha_creacion']
