from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from .models import curso, vehiculo
# Create your views here.

def home(request):
    queryset = curso.objects.all()
    return render(request, 'gestioncursos.html', {'queryset':queryset})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credito=request.POST['numCredito']

    cursos = curso.objects.create(codigo = codigo, nombre=nombre, creditos=credito)
    return redirect('/')

def edicionCurso(request, codigo):
    cursos = curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html', {'curso': cursos})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credito=request.POST['numCreditos']

    cursos = curso.objects.get(codigo=codigo)
    cursos.nombre = nombre
    cursos.creditos= credito
    cursos.save()
    return redirect('/')

def eliminarCurso(request, codigo):
    cursos = curso.objects.get(codigo=codigo)
    cursos.delete()
    return redirect('/')



def home(request):
    queryset = vehiculo.objects.all()
    return render(request, 'gestionvehiculo.html', {'queryset':queryset})

def registrarvehiculo(request):
    placa=request.POST['txtplaca']
    capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
    cilindraje=request.POST['numcilindraje']
    fecha_SOAT=request.POST['numfecha_SOAT']
    propietario=request.POST['numpropietario']
    estado=request.POST['numestado']

    
    vehiculos = vehiculo.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
    return redirect('/')

def edicionvehiculo(request, placa):
    vehiculos = vehiculo.objects.get(placa=placa)
    return render(request, 'edicionvehiculo.html', {'vehiculo': vehiculos})

def editarvehiculo(request):
    placa=request.POST['txtplaca']
    capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
    cilindraje=request.POST['numcilindraje']
    fecha_SOAT=request.POST['numfecha_SOAT']
    propietario=request.POST['numpropietario']
    estado=request.POST['numestado']

    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
    vehiculos.cilindrajes= cilindraje
    vehiculos.fecha_SOAT= fecha_SOAT
    vehiculos.propietario= propietario
    vehiculos.estado = estado
    vehiculos.save()
    return redirect('/')

def eliminarvehiculo(request, placa):
    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.delete()
    return redirect('/')