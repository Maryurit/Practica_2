from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'organizador')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'descripcion')
