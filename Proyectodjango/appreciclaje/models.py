from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    DNI=models.IntegerField()
    telefono=models.IntegerField()
    email=models.EmailField()
    usuario=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Administrador(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()

class Objeto(models.Model):
    Baterias = 1
    Organico= 2
    Papel = 3
    Plastico= 4
    Vidrio= 5
    TipodeChoice = [
        (Baterias, 'Baterias'),
        (Organico, 'Organico'),
        (Papel, 'Papel'),
        (Plastico, 'Plastico'),
        (Vidrio, 'Vidrio')
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)  
    tipo = models.IntegerField(choices=TipodeChoice)