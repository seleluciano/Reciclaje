from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    DNI=models.IntegerField(max_length=10)
    telefono=models.IntegerField(max_length=100)
    email=models.EmailField()

class Administrador(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()

class Objeto(models.Model):
    Plastico = 1
    Metal = 2
    Papel = 3
    TipodeChoice = [
        (Plastico, 'Plastico'),
        (Metal, 'Metal'),
        (Papel, 'Papel')
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)  
    tipo = models.IntegerField(choices=TipodeChoice)