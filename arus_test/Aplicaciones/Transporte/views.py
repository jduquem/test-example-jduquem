from datetime import date, datetime
from http.client import ImproperConnectionState
from operator import imod
from django import views
from django.shortcuts import render, redirect
from .models import vehiculo, solicitud
from django.views import View

class Vehiculo(View):
    template_name = 'gestionvehiculo.html'

    def get(self, request, *args, **kwargs):
        queryset = vehiculo.objects.all()
        return render(request, self.template_name, {'queryset':queryset})

    def post(self, request, *args, **kwargs):
        placa=request.POST['txtplaca']
        capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
        cilindraje=request.POST['numcilindraje']
        fecha_SOAT=request.POST['numfecha_SOAT']
        tarjeta_operacion=request.POST['numtarjeta_operacion']
        propietario=request.POST['numpropietario']
        estado=request.POST['numestado']
        vehiculo.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
        return render(request, self.template_name)


def home(request):
    return render(request, 'blank.html')

# def vehiculos(request):
#     queryset = vehiculo.objects.all()
#     return render(request, 'gestionvehiculo.html', {'queryset':queryset})

# def registrarvehiculo(request):
#     placa=request.POST['txtplaca']
#     capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
#     cilindraje=request.POST['numcilindraje']
#     fecha_SOAT=request.POST['numfecha_SOAT']
#     tarjeta_operacion=request.POST['numtarjeta_operacion']
#     propietario=request.POST['numpropietario']
#     estado=request.POST['numestado']

#     vehiculo.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
#     return redirect('vehiculos')


class UpdateVehiculo(View):

    def get(self, request, *args, **kwargs):
        vehiculos = vehiculo.objects.get(placa=placa)
        vehiculos.fecha_SOAT = datetime.strptime(str(vehiculos.fecha_SOAT), '%Y-%m-%d').strftime('%Y-%m-%d')
        vehiculos.tarjeta_operacion = datetime.strptime(str(vehiculos.tarjeta_operacion), '%Y-%m-%d').strftime('%Y-%m-%d')
        return render(request, 'edicionvehiculo.html', {'vehiculo': vehiculos})

    def post(self, request, *args, **kwargs):
        placa=request.POST['txtplaca']
        capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
        cilindraje=request.POST['numcilindraje']
        fecha_SOAT=request.POST['numfecha_SOAT']
        tarjeta_operacion=request.POST['numtarjeta_operacion']
        propietario=request.POST['numpropietario']
        estado=request.POST['numestado']

        vehiculos = vehiculo.objects.get(placa=placa)
        vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
        vehiculos.cilindraje= cilindraje
        vehiculos.fecha_SOAT= fecha_SOAT
        vehiculos.tarjeta_operacion=tarjeta_operacion
        vehiculos.propietario= propietario
        vehiculos.estado = estado
        vehiculos.save()
        return redirect('vehiculos')

# def edicionvehiculo(request, placa):
#     vehiculos = vehiculo.objects.get(placa=placa)
#     vehiculos.fecha_SOAT = datetime.strptime(str(vehiculos.fecha_SOAT), '%Y-%m-%d').strftime('%Y-%m-%d')
#     vehiculos.tarjeta_operacion = datetime.strptime(str(vehiculos.tarjeta_operacion), '%Y-%m-%d').strftime('%Y-%m-%d')
#     return render(request, 'edicionvehiculo.html', {'vehiculo': vehiculos})

# def editarvehiculo(request):
#     placa=request.POST['txtplaca']
#     capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
#     cilindraje=request.POST['numcilindraje']
#     fecha_SOAT=request.POST['numfecha_SOAT']
#     tarjeta_operacion=request.POST['numtarjeta_operacion']
#     propietario=request.POST['numpropietario']
#     estado=request.POST['numestado']

#     vehiculos = vehiculo.objects.get(placa=placa)
#     vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
#     vehiculos.cilindraje= cilindraje
#     vehiculos.fecha_SOAT= fecha_SOAT
#     vehiculos.tarjeta_operacion=tarjeta_operacion
#     vehiculos.propietario= propietario
#     vehiculos.estado = estado
#     vehiculos.save()
#     return redirect('vehiculos')

def eliminarvehiculo(request, placa):
    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.delete()
    return redirect('vehiculos')


def solicitudes(request):
    queryset = solicitud.objects.all()
    return render(request, 'gestionsolicitud.html', {'queryset':queryset})


def registrarsolicitud(request):
    punto_de_partida=request.POST['txtpunto_de_partida']
    punto_de_llegada=request.POST['txtpunto_de_llegada']
    valor= 0
    fecha= datetime.now()
    estado_solicitud= 1# request.POST['txtestado_solicitud']

    solicitud.objects.create(punto_de_partida = punto_de_partida, punto_de_llegada=punto_de_llegada, valor=valor, fecha=fecha, estado_solicitud=estado_solicitud)
    return redirect('solicitudes')

def eliminarsolicitud(request, _id):
    solicitudes = solicitud.objects.get(_id=_id)
    solicitudes.delete()
    return redirect('solicitudes')