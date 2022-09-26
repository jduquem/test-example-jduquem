from rest_framework import routers

from .viewsets import VehiculosViewset

route = routers.DefaultRouter()
route.register('vehiculo', VehiculosViewset)
urlpatterns = route.urls


