from django.db import models
from djongo import models

# Create your models here.
status_vehiculo = (
        (0, 'Deshabilitado'),
        (1, 'Habilitado'),
    )

status_solicitud = (
        (0, 'Cancelado'),
        (1, 'Pendiente'),
        (2, 'Confirmado'),
        (3, 'En transito'),
        (4, 'Finalizado'),
    )

class vehiculo(models.Model):
    _id = models.ObjectIdField()
    placa = models.CharField(verbose_name = 'Placa', max_length = 6, null = False, blank = False)
    capacidad_de_pasajeros = models.PositiveSmallIntegerField(verbose_name = 'Capacidad de pasajeros', null = False, blank = False)
    cilindraje =  models.CharField(verbose_name = 'Cilindraje', max_length = 50, null = False, blank = False)
    fecha_SOAT =  models.DateField(verbose_name = 'fecha de vigencia soat', null = False, blank = False)
    tarjeta_operacion =  models.DateField(verbose_name = 'fecha de vigencia tarjeta de operacion', null = False, blank = False)
    propietario = models.CharField( verbose_name = 'identificación del propietario', null = False, max_length = 20, blank = False)
    estado = models.PositiveSmallIntegerField(verbose_name = 'Estado del vehiculo', choices = status_vehiculo, null = False, blank = False)    
    
    
    def __str__(self):
        return self.placa

    class Meta:
        ordering = ['placa']
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"


class solicitud(models.Model):
    _id = models.ObjectIdField()
    punto_de_partida = models.CharField(verbose_name = 'Punto de partida', max_length = 200, null = False, blank = False)
    punto_de_llegada = models.CharField(verbose_name = 'Punto de llegada', max_length = 200, null = False, blank = False)
    vehiculo = models.CharField(verbose_name = 'Placa', max_length = 6, null = False, blank = False)
    valor =  models.PositiveIntegerField(verbose_name = 'Valor', null = False, blank = False)
    km = models.FloatField(verbose_name = 'Kilometros', null = False, blank = False)
    fecha =  models.DateField(verbose_name = 'Fecha', null = False, blank = False)
    estado_solicitud = models.PositiveSmallIntegerField(verbose_name = 'Estado del viaje', choices = status_solicitud, null = False, blank = False, default=0)
    
    def __str__(self):
        return self.punto_de_partida
    
    class Meta:
        ordering = ['fecha']
        verbose_name = "solicitud viaje"
        verbose_name_plural = "solicitud viajes"