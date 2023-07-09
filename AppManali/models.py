from django.db import models

# Create your models here.
class Administrativo(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
class Paciente(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
class Doctor(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    especialidad=models.CharField(max_length=40)
