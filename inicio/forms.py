from django import forms

class AnotarEquipoForm(forms.Form):
    equipo = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=50)
    edad = forms.IntegerField(required=False)