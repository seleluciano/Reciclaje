from django.shortcuts import render
from appreciclaje.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
#from django.contrib.auth.mixins import LoginRequiredMixin

def Inicio(request):
    return render(request, "index.html")


def Concientizacion(request):
    return render(request, "concientizacion.html")


def Iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "iniciosesion.html", {"mensaje": "Datos incorrectos"})

        else:

            return render(request, "iniciosesion.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "iniciosesion.html", {'form': form})


def Registrarusuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html",  {"mensaje": "Usuario Creado :)"})
    else:
        form = UserRegisterForm()

    return render(request, "registrarusuario.html", {'form': form})


def Cerrarsesion(request):
    return render(request, "cerrarsesion.html")


def Contacto(request):
    return render(request, "contacto.html")

def Buscarobjetos(request):
    if request.method == "POST":
        objeto = request.POST.get('objeto', '')
        resultados = Objeto.objects.filter(
            descripcion__icontains=objeto) | Objeto.objects.filter(tipo__icontains=objeto)
        if resultados:
            return render(request, "concientizacion.html", {"Resultados": resultados})
        else:
            return render(request, "concientizacion.html", {"buscarporobjetos": "No se encontraron objetos"})
    else:
        return HttpResponse("No se pudo realizar la búsqueda")
