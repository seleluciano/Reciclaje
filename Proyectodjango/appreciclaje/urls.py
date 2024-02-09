from django.contrib import admin
from django.urls import path
from appreciclaje import views
urlpatterns = [
    path('',views.Inicio,name="inicio"),
    path('concientizacion/',views.Concientizacion,name="concientizacion"),
    path('contacto/',views.Contacto,name="contacto"),
    path('iniciosesion/',views.Iniciosesion,name="iniciosesion"),
    path('registrarusuario/',views.Registrarusuario,name="registrarusuario"),
    path('buscarmateriales/',views.Buscarmateriales,name="buscarmateriales"),
    path('buscarobjetos/',views.Buscarobjetos,name="buscarobjetos")
]
