from django import forms

class EquipoBase(forms.Form):
    equipo = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=50)
    edad = forms.IntegerField(required=False)

class AnotarEquipoForm(EquipoBase):
    ...
    
    

class BuscarEquipoForm(forms.Form):
    equipo = forms.CharField(max_length=20, required=False)
    
    
class ModificarEquipoForm(EquipoBase):
    ...
        
       