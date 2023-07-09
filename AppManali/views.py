from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, "AppManali/inicio.html")
def administrativo(request):
    return render (request, "AppManali/administrativo.html")
def doctor(request):
    return render(request, "AppManali/doctor.html")
def paciente(request):
    return render(request, "AppManali/paciente.html")