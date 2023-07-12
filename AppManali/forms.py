from django import forms
class AdministrativoFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.IntegerField()
