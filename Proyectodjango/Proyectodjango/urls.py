from django.urls import path,include
from django.contrib import admin
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('Appreciclaje/',include('appreciclaje.urls')),
]
