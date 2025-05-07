from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaViewSet, MensajeViewSet

router = DefaultRouter()
router.register(r'salas', SalaViewSet)
router.register(r'mensajes', MensajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
