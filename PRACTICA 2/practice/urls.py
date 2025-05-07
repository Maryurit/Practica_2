from django.contrib import admin
from django.urls import path, include
from calificaciones.views import editar_calificacion, eliminar_calificacion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),  # <-- Esta línea se asegura de incluir las URLs como logout, etc.
    path('calificaciones/', include('calificaciones.urls')),
    path('editar/<int:pk>/', editar_calificacion, name='editar_calificacion'),
    path('eliminar/<int:pk>/', eliminar_calificacion, name='eliminar_calificacion'),
    path('chat/', include('chat.urls')),
    path('eventos/', include('eventos.urls')),
    path('foro/', include('foro.urls')),
    path('api/', include('usuarios.api_urls')),
    path('api/calificaciones/', include('calificaciones.api_urls')),
    path('api/chat/', include('chat.api_urls')),
    path('api/eventos/', include('eventos.api_urls')),
    path('api/foro/', include('foro.api_urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

