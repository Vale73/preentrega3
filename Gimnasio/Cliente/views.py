from django.shortcuts import render
from .models import Profesor, Alumno, Turno

def index(request):
    return render(request, 'index.html')

def pagina_principal(request):
    turnos = Turno.objects.all()
    alumnos = Alumno.objects.all()
    profesores = Profesor.objects.all()
    return render(request, 'principal.html', {'turnos': turnos, 'alumnos': alumnos, 'profesores': profesores})


def profesor_index(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor.html', {'profesores': profesores})

def alumno_index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos': alumnos})

def turno_index(request):
    turnos = Turno.objects.all()
    return render(request, 'turno.html', {'turnos': turnos})