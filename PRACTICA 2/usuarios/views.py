from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework import viewsets
from .serializers import UsuarioSerializer


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")  # O la vista principal a la que quieras dirigir
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "usuarios/login.html")


def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Asegúrate de tener 'login' en tus URLs
    else:
        form = RegistroForm()
    return render(request, 'usuarios/register.html', {'form': form})


def IndexView(request):
    '''Esto es la página principal'''
    objeto = Usuario.objects.all().order_by("-id")
    return render(request, "index.html", {"objeto": objeto})


def cerrar_sesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('index')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer