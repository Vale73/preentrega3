from django.urls import path

from . import views

app_name = "Cliente"

urlpatterns = [
    path("", views.index, name="index"),
]