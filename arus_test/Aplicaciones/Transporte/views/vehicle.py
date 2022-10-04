from datetime import date, datetime
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from ..models import vehiculo
from django.views import View


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
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        queryset = vehiculo.objects.filter(placa=request.POST['txtplaca'].upper())
        if queryset is not None:
            messages.warning(request, 'El vehiculo con placa {} ya se encuentra creado'.format(request.POST['txtplaca']))
            return HttpResponseRedirect(reverse('vehiculo'))
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
            queryset = vehiculo.objects.get(placa=kwargs['placa'])
            return render(request, self.template_name, {'vehiculo':kwargs['placa']})
        except:
            return redirect('vehicle')

    def post(self, request, *args, **kwargs):
        try:
            vehiculos = vehiculo.objects.get(placa=request.POST['txtplaca'])
            vehiculos.delete()
            return redirect('vehicle')
        except:
            return render(request, self.template_name)
