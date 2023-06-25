from django.db import models

# Create your models here.

class EquipoFutbol(models.Model):
    equipo = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)