from django.db import models
from Alumno.models import Alumno
from Profesor.models import Profesor

class Turno(models.Model):
    turno = models.CharField(max_length=8)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.turno
    









#class Turno(models.Model):
#    nombre = models.PositiveIntegerField(unique=True)
#    turno = models.ForeignKey(turno, on_delete=models.SET_NULL, null=True, blank=True)
#    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
#    Alumno = models.ManyToManyField(Alumno)




