from rest_framework import viewsets

from Aplicaciones.Transporte.models import vehiculo, solicitud

from .serializers import vehiculoSerializers, solicitudSerializers

class VehiculosViewset(viewsets.ModelViewSet):
    queryset = vehiculo.objects.all()
    serializer_class = vehiculoSerializers

class solicitudesViewset(viewsets.ModelViewSet):
    queryset = solicitud.objects.all()
    serializer_class = solicitudSerializers
