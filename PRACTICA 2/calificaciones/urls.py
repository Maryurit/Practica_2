from django.urls import path
from .views import calificaciones_view

urlpatterns = [
    path('', calificaciones_view, name='calificaciones'),
]
