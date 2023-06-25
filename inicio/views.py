from django.shortcuts import render
from inicio.forms import AnotarEquipoForm



# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def anotar_equipo(request):
    
    if request.method == 'POST':
        formulario = AnotarEquipoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
    
    
    formulario = AnotarEquipoForm()
    return render(request, 'inicio/anotar_equipo.html', {'formulario': formulario})