from rest_framework import routers

from .viewsets import VehiculosViewset, solicitudesViewset

route = routers.DefaultRouter()
route.register('vehiculo', VehiculosViewset)
route.register('solicitud', solicitudesViewset)
urlpatterns = route.urls


