from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Mensaje  # Asegúrate de importar Mensaje
from rest_framework import viewsets, permissions
from .serializers import SalaSerializer, MensajeSerializer

@login_required
def salas_view(request):
    salas = Sala.objects.all()  # Mostramos todas las salas disponibles
    return render(request, 'chat/salas.html', {'salas': salas})


@login_required
def detalle_sala_view(request, pk):
    sala = get_object_or_404(Sala, pk=pk)

    # Asegurarse de que el usuario sea participante
    if request.user not in sala.participantes.all():
        return redirect('salas')

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Mensaje.objects.create(
                sala=sala,
                remitente=request.user,
                contenido=contenido
            )
            return redirect('detalle_sala', pk=sala.pk)

    mensajes = sala.mensajes.order_by('timestamp')
    return render(request, 'chat/detalle_sala.html', {
        'sala': sala,
        'mensajes': mensajes
    })
@login_required
def unirse_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    sala.participantes.add(request.user)
    return redirect('detalle_sala', pk=pk)

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo salas donde el usuario actual participa
        return self.request.user.salas.all()

    def perform_create(self, serializer):
        sala = serializer.save()
        sala.participantes.add(self.request.user)  # Agregar al creador como participante


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar mensajes de salas en las que participa el usuario
        return Mensaje.objects.filter(sala__participantes=self.request.user)

