#from django.contrib import admin


#from . import models
#from Alumno.models import models
#from Profesor.models import models


#admin.site.register(models.Alumno)
#admin.site.register(models.Profesor)
#admin.site.register(models.turno)
#admin.site.register(models.Turno)
# Register your models here.


from django.contrib import admin
from Alumno.models import Alumno
from Profesor.models import Profesor
from Turno.models import Turno

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Turno)