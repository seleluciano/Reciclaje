from django.contrib import admin
from django.urls import path
from appreciclaje import views
urlpatterns = [
    path('',views.Inicio)
]
