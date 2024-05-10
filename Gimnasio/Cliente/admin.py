from django.contrib import admin

from . import models

admin.site.register(models.Alumno)
admin.site.register(models.Profesor)
admin.site.register(models.Turno)
# Register your models here.
