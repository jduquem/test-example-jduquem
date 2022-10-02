from django.contrib import admin
from .models import vehiculo, solicitud
from django.contrib.auth.models import Permission


# Register your models here.
admin.site.register(vehiculo)
admin.site.register(solicitud)
admin.site.register(Permission)
