from django.shortcuts import render

from . import models

def index(request):
    consulta = models.turno
    contexto = {"Turnos":consulta}
    return render(request, "cliente/index.html", contexto)

# Create your views here.
