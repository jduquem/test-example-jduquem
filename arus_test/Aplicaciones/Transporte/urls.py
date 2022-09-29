#from urllib.parse import urlparse
from django.urls import path#, re_path
from .views import Home
from .views import Vehiculo, VehiculoAdd, VehiculoUpdate, VehiculoDelete
from .views import Solicitud, SolicitudAdd, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    #vehiculo
    path('vehiculo/', Vehiculo.as_view(), name='vehiculo'),
    path('vehiculo_add/', VehiculoAdd.as_view(), name='vehiculo_add'),
    path('vehiculo_update/', VehiculoUpdate.as_view(), name='vehiculo_update'),
    path('vehiculo_delete/', VehiculoDelete.as_view(), name='vehiculo_delete'),
    #solicitud
    path('solicitud/', Solicitud.as_view(), name='solicitud'),
    path('solicitud_add/', SolicitudAdd.as_view(), name='solicitud_add'),
    path('solicitud_update/', SolicitudUpdate.as_view(), name='solicitud_update'),
    path('solicitud_delete/', SolicitudDelete.as_view(), name='solicitud_delete'),
]