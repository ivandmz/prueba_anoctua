from django.db import models

# Create your models here.
class Cotizacion(models.Model):
    fecha = models.DateField()
    tipo_de_cambio = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f'{self.fecha} - {self.tipo_de_cambio}'