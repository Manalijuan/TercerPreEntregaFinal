from django import forms
class AdministrativoFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()

class PacienteFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()    
