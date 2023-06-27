from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/anotar/', views.anotar_equipo, name='anotar_equipo'),
    path('equipos/modificar/<int:equipo_id>/', views.modificar_equipo, name='modificar_equipo'),
]
