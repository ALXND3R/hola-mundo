from django.shortcuts import render
from django.http import HttpResponse #pagina_web/views.py

# Create your views here.

def VistaPaginaDeInicio(solicitud):
    return HttpResponse("HOLA MUNDO!")