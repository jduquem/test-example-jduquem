from django.db import models
from djongo import models

# Create your models here.
status_vehiculo = (
        (0, 'Deshabilitado'),
        (1, 'Habilitado'),
    )
    
class vehiculo(models.Model):
    _id = models.ObjectIdField()
    placa = models.CharField(verbose_name = 'Placa', max_length = 6, null = False, blank = False)
    capacidad_de_pasajeros = models.PositiveSmallIntegerField(verbose_name = 'Capacidad de pasajeros', null = False, blank = False)
    cilindraje =  models.CharField(verbose_name = 'Cilindraje', max_length = 50, null = False, blank = False)
    fecha_SOAT =  models.DateField(verbose_name = 'fecha de vigencia soat', null = False, blank = False)
    tarjeta_operacion =  models.DateField(verbose_name = 'fecha de vigencia tarjeta de operacion', null = False, blank = False)
    propietario = models.CharField(verbose_name = 'identificacion del propietario', null = False, max_length = 20, blank = False)
    estado = models.PositiveSmallIntegerField(verbose_name = 'Estado del vehiculo', choices = status_vehiculo, null = False, blank = False)


    def __str__(self):
        return self.placa
    
    class Meta:
        ordering = ['placa']
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"