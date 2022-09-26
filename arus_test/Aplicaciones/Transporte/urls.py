from urllib.parse import urlparse
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('registrarvehiculo/', views.registrarvehiculo, name='registrarvehiculo'),
    path('edicionvehiculo/<placa>', views.edicionvehiculo, name='edicionvehiculo'),
    path('editarvehiculo/', views.editarvehiculo, name='editarvehiculo'),
    path('eliminarvehiculo/<placa>', views.eliminarvehiculo, name='eliminarvehiculo'),
]