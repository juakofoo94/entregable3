from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipos/anotar/', views.anotar_equipo, name='anotar_equipo')
]
