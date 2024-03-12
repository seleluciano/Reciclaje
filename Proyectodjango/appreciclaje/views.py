from django.shortcuts import render
from appreciclaje.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def Inicio(request):
    return render(request, "index.html")

@login_required
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


@login_required
def Contacto(request):
    return render(request, "contacto.html")


@login_required
def Editarperfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "perfil.html")

    else:

        miFormulario = UserRegisterForm(initial={'email': usuario.email})

    return render(request, "perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class Listarobjeto(LoginRequiredMixin,ListView):
    model=Objeto
    template_name="objeto_list.html"
    

class Crearobjeto(LoginRequiredMixin,CreateView):
    model=Objeto
    fields=['nombre','descripcion','tipo']
    template_name="objeto_form.html"  

class Modificarobjeto(LoginRequiredMixin,UpdateView):
    model=Objeto
    fields=['nombre','descripcion','tipo']
    template_name="objeto_form.html"

class Eliminarobjeto(LoginRequiredMixin,DeleteView):
    model=Objeto
    template_name="objeto_confirm_delete.html"
class Detalleobjeto(LoginRequiredMixin,DetailView):
   model=Objeto
   template_name="objeto_detalle.html"
