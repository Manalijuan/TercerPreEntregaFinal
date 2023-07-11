from django.urls import path
from AppManali import views
urlpatterns= [
    path("",views.inicio, name="Inicio"),
    path("administrativo",views.administrativo, name="Administrativo"),
    path("doctor",views.doctor, name="Doctor"),
    path("paciente",views.paciente, name="Paciente"),
    path("formulario",views.formulario, name="Formulario")

]