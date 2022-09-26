from rest_framework import viewsets

from Aplicaciones.Academico.models import vehiculo

from .serializers import vehiculoSerializers

class VehiculosViewset(viewsets.ModelViewSet):
    queryset = vehiculo.objects.all()
    serializer_class = vehiculoSerializers