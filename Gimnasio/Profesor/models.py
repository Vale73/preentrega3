from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    turno = models.CharField(max_length=10, choices=(('Mañana', 'Mañana'), ('Tarde', 'Tarde')))

    def __str__(self):
        return self.nombre