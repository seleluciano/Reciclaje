from django.contrib import admin
from django.urls import path
from Proyectodjango.views import Saludo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Saludo/',Saludo),
]
