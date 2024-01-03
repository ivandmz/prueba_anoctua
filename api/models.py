from django.db import models

# Create your models here.
class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    tipo_de_cambio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.fecha} - {self.tipo_de_cambio}'
    
    class Meta:
        db_table = 'cotizaciones'


class Compra(models.Model):
    cotizacion = models.ForeignKey(Cotizacion,on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_compra = models.DateField()

    def __str__(self):
        return f'${self.monto} - {self.fecha_de_compra} - u$s{self.cotizacion}'
    
    class Meta:
        db_table = 'compras'