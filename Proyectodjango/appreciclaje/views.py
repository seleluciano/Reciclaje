from django.shortcuts import render

def Inicio(request):
    return render(request, "index.html")

def Concientizacion(request):
    return render(request, "concientizacion.html")

def Iniciosesion(request):
    return render(request, "iniciosesion.html")

def Registrarusuario(request):
    return render(request, "registrarusuario.html")

def Contacto(request):
    return render(request, "contacto.html")
