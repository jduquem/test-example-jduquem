from datetime import date, datetime
import random
from django.contrib import messages
#from http.client import ImproperConnectionState
#from operator import imod
#from django import views
from django.contrib.auth import login
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from .models import vehiculo, solicitud
from django.views import View
from Aplicaciones.Transporte.forms import UserRegisterForm


#Clave API : AIzaSyB0CdWrNiCOjzJ4Ogq6c1VzK1KqXkez3ko
class Home(View):
    template_name = 'blank.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

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


# class UpdateVehiculo(View):

#     def get(self, request, *args, **kwargs):
#         vehiculos = vehiculo.objects.get(placa=placa)
#         vehiculos.fecha_SOAT = datetime.strptime(str(vehiculos.fecha_SOAT), '%Y-%m-%d').strftime('%Y-%m-%d')
#         vehiculos.tarjeta_operacion = datetime.strptime(str(vehiculos.tarjeta_operacion), '%Y-%m-%d').strftime('%Y-%m-%d')
#         return render(request, 'edicionvehiculo.html', {'vehiculo': vehiculos})

#     def post(self, request, *args, **kwargs):
#         placa=request.POST['txtplaca']
#         capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
#         cilindraje=request.POST['numcilindraje']
#         fecha_SOAT=request.POST['numfecha_SOAT']
#         tarjeta_operacion=request.POST['numtarjeta_operacion']
#         propietario=request.POST['numpropietario']
#         estado=request.POST['numestado']

#         vehiculos = vehiculo.objects.get(placa=placa)
#         vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
#         vehiculos.cilindraje= cilindraje
#         vehiculos.fecha_SOAT= fecha_SOAT
#         vehiculos.tarjeta_operacion=tarjeta_operacion
#         vehiculos.propietario= propietario
#         vehiculos.estado = estado
#         vehiculos.save()
#         return redirect('vehiculos')

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

# def eliminarvehiculo(request, placa):
#     vehiculos = vehiculo.objects.get(placa=placa)
#     vehiculos.delete()
#     return redirect('vehiculos')


# def solicitudes(request):
#     queryset = solicitud.objects.all()
#     return render(request, 'gestionsolicitud.html', {'queryset':queryset})


# def registrarsolicitud(request):
#     punto_de_partida=request.POST['txtpunto_de_partida']
#     punto_de_llegada=request.POST['txtpunto_de_llegada']
#     valor= 0
#     fecha= datetime.now()
#     estado_solicitud= 1# request.POST['txtestado_solicitud']

#     solicitud.objects.create(punto_de_partida = punto_de_partida, punto_de_llegada=punto_de_llegada, valor=valor, fecha=fecha, estado_solicitud=estado_solicitud)
#     return redirect('solicitudes')

# def eliminarsolicitud(request, _id):
#     solicitudes = solicitud.objects.get(_id=_id)
#     solicitudes.delete()
#     return redirect('solicitudes')


class Vehiculo(View):
    template_name = 'vehiculo.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = vehiculo.objects.all()
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

class VehiculoAdd(View):
    template_name = 'vehiculo_add.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = vehiculo.objects.all()
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        queryset = vehiculo.objects.all()
        for p in queryset:
            if p == request.POST['txtplaca']:
                messages.warning(request, 'El vehiculo con placa {} ya se encuentra creado'.format(request.POST['txtplaca']))
                return render(request, self.template_name)
            else:
                try:
                    placa=request.POST['txtplaca'].upper()
                    capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
                    cilindraje=request.POST['numcilindraje']
                    fecha_SOAT=request.POST['numfecha_SOAT']
                    tarjeta_operacion=request.POST['numtarjeta_operacion']
                    propietario=request.POST['numpropietario']
                    estado=request.POST['numestado']
                    vehiculo.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
                    #messages.success(request, 'Se ha creado el vehículo con placa {}'.format(placa))
                    return HttpResponseRedirect(reverse('vehiculo'))
                except:
                    return render(request, self.template_name)

class VehiculoUpdate(View):
    template_name = 'vehiculo_update.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = vehiculo.objects.all()
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            placa=request.POST['txtplaca']
            capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
            cilindraje=request.POST['numcilindraje']
            fecha_SOAT=request.POST['numfecha_SOAT']
            tarjeta_operacion=request.POST['numtarjeta_operacion']
            propietario=request.POST['numpropietario']
            estado=request.POST['numestado']

            vehiculos = vehiculo.objects.get(placa=kwargs['placa'])
            vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
            vehiculos.cilindraje= cilindraje
            vehiculos.fecha_SOAT= fecha_SOAT
            vehiculos.tarjeta_operacion=tarjeta_operacion
            vehiculos.propietario= propietario
            vehiculos.estado = estado
            vehiculos.save()
            return HttpResponseRedirect(reverse('vehiculo',))
        except:
            return render(request, self.template_name)

class VehiculoDelete(View):
    template_name = 'vehiculo_delete.html'

    def get(self, request, *args, **kwargs):
        try:
            vehiculos = vehiculo.objects.get(placa=args)
            vehiculos.delete()
            messages.warning(request, 'El vehiculo con placa {} se elimino correctamente'.format(args))
            return render(request, self.template_name)
        except:
            return render(request, self.template_name)

class Solicitud(View):
    template_name = 'solicitud.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = solicitud.objects.filter(estado_solicitud=1)
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

class SolicitudEnd(View):
    template_name = 'solicitud_end.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = solicitud.objects.filter(estado_solicitud=4)
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)


class SolicitudCancel(View):
    template_name = 'solicitud_cancel.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = solicitud.objects.filter(estado_solicitud=0)
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

class SolicitudTransit(View):
    template_name = 'solicitud_transit.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = solicitud.objects.filter(estado_solicitud=3)
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)
    
class SolicitudAdd(View):
    template_name = 'solicitud_add.html'

    def get(self, request, *args, **kwargs):
        try:
            queryset = solicitud.objects.all()
            return render(request, self.template_name, {'queryset':queryset})
        except:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            punto_de_partida=request.POST['txtpunto_de_partida']
            punto_de_llegada=request.POST['txtpunto_de_llegada']
            km = random.randint(10, 30)
            valor= km * 1100 
            fecha= datetime.now()
            estado_solicitud= 3# request.POST['txtestado_solicitud']
            solicitud.objects.create(punto_de_partida = punto_de_partida, punto_de_llegada=punto_de_llegada, valor=valor, fecha=fecha, estado_solicitud=estado_solicitud, km = km)
            #messages.success(request, 'La solicitud fue creada con exito')
            return HttpResponseRedirect(reverse('solicitud'))
        except:
            return render(request, self.template_name)

# class SolicitudAdd(View):
#     template_name = 'solicitud_add.html'

#     def get(self, request, *args, **kwargs):
#         try:
#             queryset = solicitud.objects.all()
#             return render(request, self.template_name, {'queryset':queryset})
#         except:
#             return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         try:
#             punto_de_partida=request.POST['txtpunto_de_partida']
#             punto_de_llegada=request.POST['txtpunto_de_llegada']
#             km = random.randint(10, 30)
#             valor= float(km) * 1100
#             import pdb; pdb.set_trace()
#             fecha= datetime.now()
#             estado_solicitud= 1# request.POST['txtestado_solicitud']
#             solicitud.objects.create(punto_de_partida = punto_de_partida, punto_de_llegada=punto_de_llegada, valor=valor, fecha=fecha, estado_solicitud=estado_solicitud, km = km)
#             return render(request, self.template_name, {'result':'ok'})
#         except:
#             return render(request, self.template_name)

# class SolicitudUpdate(View):
#     template_name = 'Solicitud_update.html'

#     def get(self, request, *args, **kwargs):
#         try:
#             queryset = solicitud.objects.all()
#             return render(request, self.template_name, {'queryset':queryset})
#         except:
#             return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         try:
#             placa=request.POST['txtplaca']
#             capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
#             cilindraje=request.POST['numcilindraje']
#             fecha_SOAT=request.POST['numfecha_SOAT']
#             tarjeta_operacion=request.POST['numtarjeta_operacion']
#             propietario=request.POST['numpropietario']
#             estado=request.POST['numestado']
#             solicitud.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
#             return render(request, self.template_name, {'result':'ok'})
#         except:
#             return render(request, self.template_name)

# class SolicitudDelete(View):
#     template_name = 'solicitud_delete.html'

#     def get(self, request, *args, **kwargs):
#         try:
#             queryset = solicitud.objects.all()
#             return render(request, self.template_name, {'queryset':queryset})
#         except:
#             return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         try:
#             placa=request.POST['txtplaca']
#             capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
#             cilindraje=request.POST['numcilindraje']
#             fecha_SOAT=request.POST['numfecha_SOAT']
#             tarjeta_operacion=request.POST['numtarjeta_operacion']
#             propietario=request.POST['numpropietario']
#             estado=request.POST['numestado']
#             solicitud.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
#             return render(request, self.template_name, {'result':'ok'})
#         except:
#             return render(request, self.template_name)


class RegisterUser(View):
    template_name = 'signup.html'    
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        print('registro')
        if form.is_valid():

            user = form.save()
            login(request, user)
            username = form.cleaned_data['username']
            #messages.success(request, 'Usuario {} creado con exito.'.format(username))
            return redirect('vehiculo')
        else:
            print('error de registro')
        return render(request, self.template_name, {'form': form})
