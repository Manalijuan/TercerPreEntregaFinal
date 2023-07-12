from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppManali.forms import AdministrativoFormulario
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
        miformulario=AdministrativoFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data

        administrativo=Administrativo(nombre=informacion["nombre"],apellido=informacion["apellido"])
        administrativo.save()
        return render(request, "AppManali/inicio.html")
    else:
        miformulario=AdministrativoFormulario()
    return render(request, "AppManali/administrativoFormulario.html",{"miformulario":miformulario})
