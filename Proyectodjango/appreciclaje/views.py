from django.shortcuts import render
from appreciclaje.models import *
from django.http import HttpResponse

def Inicio(request):
    return render(request, "index.html")

def Concientizacion(request):
    return render(request, "concientizacion.html")

def Iniciosesion(request):
    return render(request, "iniciosesion.html")

def Registrarusuario(request):
    if request.method == "POST":
        cliente=Cliente(request.POST['nombre'],request.POST['apellido'],request.POST['DNI'],request.POST['email'],request.POST['usuario'],request.POST['password'])
        cliente.save()
        return(HttpResponse("Usuario creado con exito, Bienvenido!!"))
    
    return render(request, "registrarusuario.html")

def Contacto(request):
    return render(request, "contacto.html")

def Buscarmateriales(request):
    if request.method == "POST":
        tipo = request.POST.get('tipo', '')
        objetos = Objeto.objects.filter(tipo__icontains=tipo) 
        return render(request, "concientizacion.html", {"Materiales": objetos})
    else:
         return(HttpResponse("No se pudo realizar la busqueda"))
    
def Buscarobjetos(request):
    if request.method == "POST":
        objeto = request.POST.get('objeto', '')
        descripcion = Objeto.objects.filter(descripcion__icontains=objeto) 
        tipo = Objeto.objects.filter(tipo__icontains=objeto)
        return render(request, "concientizacion.html", {"Objeto": objeto, "Descripcion": descripcion, "Tipo": tipo})
    else:
         return(HttpResponse("No se pudo realizar la busqueda"))