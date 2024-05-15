from django.db import models

from Profesor.models import Profesor
from Alumno.models import Alumno

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    alumnos = models.ManyToManyField(Alumno)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre