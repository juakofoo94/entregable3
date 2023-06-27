from django.shortcuts import render, redirect
from inicio.forms import AnotarEquipoForm, BuscarEquipoForm, ModificarEquipoForm
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


def modificar_equipo(request, equipo_id):
    equipo_a_modificar = EquipoFutbol.objects.get(id=equipo_id) 
    
    if request.method == 'POST':
        formulario = ModificarEquipoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            equipo_a_modificar.equipo = info['equipo']
            equipo_a_modificar.ciudad = info['ciudad']
            equipo_a_modificar.edad = info['edad']
            equipo_a_modificar.save()
            return redirect('inicio:listar_equipos')
        else:
            return render ('inicio/modificar_equipos.html', {'formulario': formulario})  
    
                
    formulario = ModificarEquipoForm(initial={'nombre': equipo_a_modificar.equipo, 'ciudad': equipo_a_modificar.ciudad, 'edad': equipo_a_modificar.ciudad})
    return render ('inicio/modificar_equipos.html', {'formulario': formulario})  
    