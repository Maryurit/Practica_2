from django.urls import path
from .views import IndexView, login_view, register_view
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .views import cerrar_sesion


# Vista personalizada para logout con mensaje
class CustomLogoutView(LogoutView):
    next_page = 'index'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Sesión cerrada exitosamente.")
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('', IndexView, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', cerrar_sesion, name='logout'),
]
