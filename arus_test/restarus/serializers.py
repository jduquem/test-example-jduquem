# from rest_framework import serializers
from rest_framework import serializers
from Aplicaciones.Transporte.models import vehiculo, solicitud

class vehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = ['_id','placa', 'capacidad_de_pasajeros', 'cilindraje', 'tarjeta_operacion', 'fecha_SOAT', 'propietario', 'estado']
    
class solicitudSerializers(serializers.ModelSerializer):
    class Meta:
        model = solicitud
        fields = ['_id','punto_de_partida', 'punto_de_llegada', 'vehiculo', 'valor', 'fecha', 'estado_solicitud']