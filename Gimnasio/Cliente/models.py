from django.db import models

# Create your models here.
class turno(models.Model):

    Turno = models.CharField(max_length=1)


    def __str__(self) -> str:
        return self.Turno
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nombre

class Turno(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    turno = models.ForeignKey(turno, on_delete=models.SET_NULL, null=True, blank=True)
    Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
    Alumno = models.ManyToManyField(Alumno)