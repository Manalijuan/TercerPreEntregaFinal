from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppManali.forms import *
# Create your views here.
def inicio(request):
    return render(request, "AppManali/inicio.html")
#def administrativo(request):
   # return render (request, "AppManali/administrativo.html")
def doctor(request):
    return render(request, "AppManali/doctor.html")
def paciente(request):
    return render(request, "AppManali/busquedaPaciente.html")

def administrativo(request):

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

def pacienteFormulario(request):
    if request.method=="POST":
        miformulario=PacienteFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            
        paciente=Paciente(nombre=informacion["nombre"],
                            apellido=informacion["apellido"],
                            email=informacion["email"])
        paciente.save()
        return render(request,"AppManali/inicio.html")
    else:
        miformulario=PacienteFormulario()
    return render(request,"AppManali/pacienteFormulario.html",{"miformulario":miformulario})

def busquedaPaciente(request):
    return render(request, "AppManali/paciente.html")
def buscar(request):
    if request.GET["nombre"]:
    #respuesta=f"Estoy buscando el Paciente: {request.GET['nombre']}"
        nombre=request.GET["nombre"]
        nombre=Paciente.objects.filter(nombre__icontains=nombre)
        return render(request, "AppManali/resultadoBusqueda.html", {"nombre":nombre})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)