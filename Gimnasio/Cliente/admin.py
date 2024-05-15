from django.contrib import admin

from . import models

admin.site.register(models.Turno)
admin.site.register(models.Profesor)
admin.site.register(models.Alumno)

