from django.shortcuts import render
from inicio.forms import AnotarEquipoForm, BuscarEquipoForm
from inicio.models import EquipoFutbol


# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def anotar_equipo(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = AnotarEquipoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            equipo = EquipoFutbol(nombre=info['nombre'], ciudad=info['ciudad'], edad=info['edad'])
            equipo.save()    
            mensaje = 'Tus datos se registraron correctamente'
        
        
        else:
            return render(request, 'inicio/anotar_equipo.html', {'formulario': formulario})
    
    formulario = AnotarEquipoForm()
    return render(request, 'inicio/anotar_equipo.html', {'formulario': formulario, 'mensaje': mensaje})

def listar_equipos(request):
    formulario = BuscarEquipoForm(request.GET)
    if formulario.is_valid():
        equipo_a_buscar = formulario.cleaned_data['equipo']
        listado_de_equipos = EquipoFutbol.objects.filter(equipo__icontains=equipo_a_buscar)
    
      
    return render(request, 'inicio/listar_equipos.html', {'formulario': formulario, 'equipos': listado_de_equipos})