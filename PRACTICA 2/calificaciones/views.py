from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia, Calificacion
from .forms import CalificacionForm
from django.contrib import messages
from .serializers import MateriaSerializer, CalificacionSerializer
from rest_framework import viewsets

@login_required
def calificaciones_view(request):
    calificaciones = Calificacion.objects.all()

    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.usuario = request.user  # Asigna el usuario actual
            calificacion.save()
            messages.success(request, "Calificación agregada correctamente.")
            return redirect('calificaciones')
    else:
        form = CalificacionForm()

    return render(request, 'calificaciones/calificaciones.html', {
        'calificaciones': calificaciones,
        'form': form
    })



@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Calificación actualizada correctamente.")
            return redirect('calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar_calificacion.html', {'form': form})


@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        messages.success(request, "Calificación eliminada correctamente.")
        return redirect('calificaciones')
    return render(request, 'calificaciones/eliminar_calificacion.html', {'calificacion': calificacion})


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer