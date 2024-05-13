from django.db import models

# Create your models here.
class turno(models.Model):

    turno = models.CharField(max_length=1)


    def __str__(self) -> str:
        return self.turno
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.nombre