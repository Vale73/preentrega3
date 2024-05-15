from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=8, unique=False)

    def __str__(self) -> str:
        return self.nombre


class Turno(models.Model):
    nombre = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nombre


#class Turno(models.Model):
#    nombre = models.PositiveIntegerField(unique=True)
#    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True, blank=True)
#    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
#    alumno = models.ManyToManyField(Alumno)