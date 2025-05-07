from django.urls import path
from .views import salas_view, detalle_sala_view, unirse_sala  # detalle_sala_view lo implementaremos después

urlpatterns = [
    path('', salas_view, name='salas'),
    path('<int:pk>/', detalle_sala_view, name='detalle_sala'),
    path('<int:pk>/unirse/', unirse_sala, name='unirse_sala'),
]
