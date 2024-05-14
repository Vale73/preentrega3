#from django.db import models

# Create your models here.
#class turno(models.Model):

#    turno = models.CharField(max_length=8)


#    def __str__(self) -> str:
#        return self.turno
    
#class Alumno(models.Model):
#    nombre = models.CharField(max_length=8)

#    def __str__(self) -> str:
#        return self.nombre
    
#class Profesor(models.Model):
#    nombre = models.CharField(max_length=8)

#    def __str__(self) -> str:
#        return self.nombre
    

from django.db import models

class Turno(models.Model):
    turno = models.CharField(max_length=8)
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE, null=True)  # Establecer un valor predeterminado, como None
    alumnos = models.ManyToManyField('Alumno')

    def __str__(self):
        return self.turno

class Alumno(models.Model):
    nombre = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre






#class Turno(models.Model):
#    nombre = models.PositiveIntegerField(unique=True)
#    turno = models.ForeignKey(turno, on_delete=models.SET_NULL, null=True, blank=True)
#    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
#    Alumno = models.ManyToManyField(Alumno)
