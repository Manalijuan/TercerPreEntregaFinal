from django.db import models

# Create your models here.
class Administrativo(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    def __str__(self):
        texto="{0} {1}"
        return texto.format(self.nombre,self.apellido)
class Paciente(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    def __str__(self):
        texto="{0} {1} {2}"
        return texto.format(self.nombre,self.apellido,self.email)
class Doctor(models.Model):
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    especialidad=models.CharField(max_length=40)
    def __str__(self):
        texto="{0} {1} ({2})"
        return texto.format(self.nombre,self.apellido,self.especialidad)
