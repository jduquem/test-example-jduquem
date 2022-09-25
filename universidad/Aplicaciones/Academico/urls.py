from urllib.parse import urlparse
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('registrarvehiculo/', views.registrarvehiculo),
    path('edicionvehiculo/<placa>', views.edicionvehiculo),
    path('editarvehiculo/', views.editarvehiculo),
    path('eliminarvehiculo/<placa>', views.eliminarvehiculo)
]