from django.db import models

# Create your models here.
class Cotizacion(models.Model):
    fecha = models.DateField()
    tipo_de_cambio =