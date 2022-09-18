from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from .models import curso
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