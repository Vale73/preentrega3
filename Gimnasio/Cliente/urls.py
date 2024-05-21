from django.urls import path

from . import views

app_name = "Cliente"

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path("profesores/", views.profesor_index, name="profesor_index"),
    path("alumnos/", views.alumno_index, name="alumno_index"),
    path("turnos/", views.turno_index, name="turno_index"),
]