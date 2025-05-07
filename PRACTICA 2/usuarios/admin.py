from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.site_header = "Hola"
admin.site.index_title = "Hola2"
admin.site.site_title = "Hola3"

class UsuarioAdmin(admin.ModelAdmin):
    fields =["nombre","fecha_nacimiento", "telefono", "direccion"]
    list_display = ["nombre","fecha_nacimiento", "telefono", "direccion"]

admin.site.register(Usuario,UsuarioAdmin)