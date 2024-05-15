from django.db import models

from Profesor.models import models
from Alumno.models import models

#class Turno(models.Model):
#    nombre = models.CharField(max_length=100)
#    alumnos = models.ManyToManyField(Alumno)
#    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.nombre
    



class Turno(models.Model):
    turno = models.CharField(max_length=8)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, related_name='turnos_asignados')
    alumnos = models.ManyToManyField('Alumno', related_name='turnos_asignados')

    def __str__(self):
        return self.turno

#class Alumno(models.Model):
#    nombre = models.CharField(max_length=8)

#    def __str__(self):
#        return self.nombre
    
#class Profesor(models.Model):
#    nombre = models.CharField(max_length=8)

#    def __str__(self):
#        return self.nombre