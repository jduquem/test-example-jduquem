from rest_framework import routers

from .viewsets import VehiculosViewset

route = routers.SimpleRouter()
route.register('vehiculo', VehiculosViewset)
urlpatterns = route.urls    