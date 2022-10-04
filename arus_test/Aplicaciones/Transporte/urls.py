#from urllib.parse import urlparse
from django.urls import path#, re_path
from .views.views import Home
# from .views.vehicle import Vehiculo, VehiculoAdd, VehiculoUpdate, VehiculoDelete
# from .views import Solicitud, SolicitudAdd, SolicitudEnd, SolicitudCancel, SolicitudTransit
from .views.user import RegisterUser, LoginUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),

    #vehiculo
#    path('vehiculo/', Vehiculo.as_view(), name='vehiculo'),
#    path('vehiculo_add/', VehiculoAdd.as_view(), name='vehiculo_add'),
#    path('vehiculo_update/<placa>', VehiculoUpdate.as_view(), name='vehiculo_update'),
#    path('vehiculo_delete/<placa>', VehiculoDelete.as_view(), name='vehiculo_delete'),
    #solicitud
#    path('solicitud/', Solicitud.as_view(), name='solicitud'),
#    path('solicitud_end/', SolicitudEnd.as_view(), name='solicitud_end'),
#    path('solicitud_cancel/', SolicitudCancel.as_view(), name='solicitud_cancel'),
#    path('solicitud_transit/', SolicitudTransit.as_view(), name='solicitud_transit'),
#    path('solicitud_add/', SolicitudAdd.as_view(), name='solicitud_add'),
    # path('solicitud_update/', SolicitudUpdate.as_view(), name='solicitud_update'),
    # path('solicitud_delete/', SolicitudDelete.as_view(), name='solicitud_delete'),
]