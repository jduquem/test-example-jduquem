#from urllib.parse import urlparse
from django.urls import path#, re_path
from .views import Home
from .views import Vehiculo, VehiculoAdd, VehiculoUpdate, VehiculoDelete
from .views import Solicitud, SolicitudAdd

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    #vehiculo
    path('vehiculo/', Vehiculo.as_view(), name='vehiculo'),
    path('vehiculo_add/', VehiculoAdd.as_view(), name='vehiculo_add'),
    path('vehiculo_update/(?P<placa>\d+)/$', VehiculoUpdate.as_view(), name='vehiculo_update'),
    path('vehiculo_delete/(?P<placa>\d+)/$', VehiculoDelete.as_view(), name='vehiculo_delete'),
    #solicitud
    path('solicitud/', Solicitud.as_view(), name='solicitud'),
    path('solicitud_add/', SolicitudAdd.as_view(), name='solicitud_add'),
    # path('solicitud_update/', SolicitudUpdate.as_view(), name='solicitud_update'),
    # path('solicitud_delete/', SolicitudDelete.as_view(), name='solicitud_delete'),
]