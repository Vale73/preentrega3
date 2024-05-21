from django.shortcuts import render

from . import models

def index(request):
    consulta = models.turno.objects.all()
    contexto = {"Turnos":consulta}
    return render(request, "cliente/index.html", contexto)

# Create your views here.

def profesor_index(request):
    profesores: Profesor.objects.all()
    return render (request, "profesor.html", {"profesores": profesores})


def alumno_index(request):
    alumnos: Alumno.objects.all()
    return render (request, "alumno.html", {"alumnos": alumnos})


def turno_index(request):
    turnos: Turno.objects.all()
    return render (request, "turno.html", {"turnos": turnos})