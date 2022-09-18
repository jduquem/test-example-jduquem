from re import template
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'gestioncursos.html')
