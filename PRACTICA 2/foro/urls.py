from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('categoria/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/<int:categoria_id>/responder/', views.crear_respuesta, name='crear_respuesta'),
    path('respuesta/<int:respuesta_id>/eliminar/', views.eliminar_respuesta, name='eliminar_respuesta'),

]
