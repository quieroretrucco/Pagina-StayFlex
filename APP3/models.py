from django.db import models

# Create your models here.
class Departamento(models.Model):
    barrio=models.CharField(max_length=40)
    piso=models.IntegerField()
    depto=models.CharField(max_length=40)

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
   
class Huesped(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    nacionalidad = models.CharField(max_length=30)
   
class Estadia(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
