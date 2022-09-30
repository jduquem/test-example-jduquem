from django.contrib import admin
from .models import vehiculo, solicitud, propietario
# Register your models here.
admin.site.register(vehiculo)
admin.site.register(solicitud)
admin.site.register(propietario)