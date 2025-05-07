from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
]
