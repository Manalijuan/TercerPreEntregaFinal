from django.urls import path
from AppManali import views
urlpatterns= [
    path("",views.inicio, name="Inicio"),
    path("administrativo",views.administrativo, name="Administrativo"),
    path("doctor",views.doctor, name="Doctor"),
    path("paciente",views.paciente, name="Paciente"),
    path("administrativoFormulario",views.administrativoFormulario, name="administrativoFormulario"),
    path("pacienteFormulario",views.pacienteFormulario, name="pacienteFormulario"),
    path("busquedaPaciente",views.busquedaPaciente, name="BusquedaPaciente"),
    path("buscar/",views.buscar),
]