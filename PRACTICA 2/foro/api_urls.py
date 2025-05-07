from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import CategoriaViewSet, RespuestaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

respuestas_router = NestedDefaultRouter(router, r'categorias', lookup='categoria')
respuestas_router.register(r'respuestas', RespuestaViewSet, basename='categoria-respuestas')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(respuestas_router.urls)),
]
