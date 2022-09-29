from urllib.parse import urlparse
from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.home),
    re_path(r'^vehiculo/$', views.Vehiculo.as_view(), name='vehiculo'),
    re_path(r'^UpdateVehiculo/$', views.UpdateVehiculo.as_view(), name='UpdateVehiculo'),
    path('vehiculos', views.vehiculo, name='vehiculos'),
    path('registrarvehiculo/', views.registrarvehiculo, name='registrarvehiculo'),
    path('edicionvehiculo/<placa>', views.edicionvehiculo, name='edicionvehiculo'),
    path('editarvehiculo/', views.editarvehiculo, name='editarvehiculo'),
    path('eliminarvehiculo/<placa>', views.eliminarvehiculo, name='eliminarvehiculo'),
    path('solicitudes', views.solicitudes, name='solicitudes'),
    path('registrarsolicitud/', views.registrarsolicitud, name='registrarsolicitud'),
    # path('edicionsolicitud/<id>', views.edicionsolicitud, name='edicionsolicitud'),
    # path('editarsolicitud/', views.editarsolicitud, name='editarsolicitud'),
    path('eliminarsolicitud/<id>', views.eliminarsolicitud, name='eliminarsolicitud'),
]