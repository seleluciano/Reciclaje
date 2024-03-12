from django.urls import path
from appreciclaje import views
urlpatterns = [
    path('',views.Inicio,name="inicio"),
    path('concientizacion/',views.Concientizacion,name="concientizacion"),
    path('contacto/',views.Contacto,name="contacto"),
    path('iniciosesion/',views.Iniciosesion,name="iniciosesion"),
    path('registrarusuario/',views.Registrarusuario,name="registrarusuario"),
    path('editarperfil/',views.Editarperfil,name="editarperfil"),
    path('nuevo/', views.Crearobjeto.as_view(), name="New"),
    path('objeto/list', views.Listarobjeto.as_view(), name="List"),
    path('<int:pk>', views.Detalleobjeto.as_view(), name="Detail"),
    path('editar/<int:pk>', views.Modificarobjeto.as_view(), name="Edit"),
    path('borrar/<int:pk>', views.Eliminarobjeto.as_view(), name="Delete"),
]
