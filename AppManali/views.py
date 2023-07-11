from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def inicio(request):
    return render(request, "AppManali/inicio.html")
def administrativo(request):
    return render (request, "AppManali/administrativo.html")
def doctor(request):
    return render(request, "AppManali/doctor.html")
def paciente(request):
    return render(request, "AppManali/paciente.html")
def administrativoFormulario(request):
    if request.method=="POST":
        administrativo=Administrativo(request.POST["Nombre"],
                                      request.POST["Edad"],
                                      request.POST["DNI"],
                                      request.POST["Dirección"],
                                      request.POST["Teléfono"])
        administrativo.save()
        return render(request, "inicio.html")
    return render(request,"AppManali/administrativoFormulario")
