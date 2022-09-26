# from rest_framework import serializers
from rest_framework import serializers
from Aplicaciones.Academico.models import vehiculo




class vehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = ['_id','placa', 'capacidad_de_pasajeros', 'cilindraje', 'fecha_SOAT', 'propietario', 'estado']
    