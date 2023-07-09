from django.urls import path
from AppManali import views
urlpatterns= [
    path("",views.inicio),
    path("administrativo",views.administrativo),
    path("doctor",views.doctor),
    path("paciente",views.paciente),

]