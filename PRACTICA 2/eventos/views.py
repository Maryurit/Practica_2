from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .serializers import EventoSerializer

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = request.user
            evento.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.user != evento.organizador:
        return redirect('lista_eventos')

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/editar_evento.html', {'form': form})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.user == evento.organizador:
        evento.delete()
    return redirect('lista_eventos')

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizador=self.request.user)

    def get_queryset(self):
        return Evento.objects.all().order_by('-fecha')