from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categoria, Respuesta
from .forms import RespuestaForm
from rest_framework import viewsets, permissions
from .serializers import CategoriaSerializer, RespuestaSerializer

# Lista de todas las categorías
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'foro/lista_categorias.html', {'categorias': categorias})

# Vista de una categoría con todas las respuestas (como un foro grupal)
@login_required
def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    respuestas = Respuesta.objects.filter(categoria=categoria).order_by('-fecha_creacion')

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.autor = request.user
            respuesta.categoria = categoria
            respuesta.save()
            return redirect('detalle_categoria', categoria_id=categoria.id)
    else:
        form = RespuestaForm()

    return render(request, 'foro/detalle_categoria.html', {
        'categoria': categoria,
        'respuestas': respuestas,
        'form': form
    })

@login_required
def crear_respuesta(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.autor = request.user
            respuesta.categoria = categoria
            respuesta.save()
            return redirect('detalle_categoria', categoria_id=categoria.id)
    else:
        form = RespuestaForm()

    return render(request, 'foro/crear_respuesta.html', {'form': form, 'categoria': categoria})

@login_required
def eliminar_respuesta(request, respuesta_id):
    respuesta = get_object_or_404(Respuesta, id=respuesta_id)

    if request.user != respuesta.autor:
        messages.error(request, "No tienes permiso para eliminar esta respuesta.")
        return redirect('detalle_categoria', categoria_id=respuesta.categoria.id)

    if request.method == "POST":
        categoria_id = respuesta.categoria.id
        respuesta.delete()
        messages.success(request, "Respuesta eliminada correctamente.")
        return redirect('detalle_categoria', categoria_id=categoria_id)

    return render(request, "foro/confirmar_eliminacion.html", {"respuesta": respuesta})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Respuesta.objects.filter(categoria_id=self.kwargs['categoria_pk']).order_by('-fecha_creacion')

    def perform_create(self, serializer):
        categoria = Categoria.objects.get(pk=self.kwargs['categoria_pk'])
        serializer.save(autor=self.request.user, categoria=categoria)