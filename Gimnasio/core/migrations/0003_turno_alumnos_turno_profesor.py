# Generated by Django 5.0.6 on 2024-05-14 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_alumno_nombre_alter_profesor_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='alumnos',
            field=models.ManyToManyField(to='core.alumno'),
        ),
        migrations.AddField(
            model_name='turno',
            name='profesor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.profesor'),
        ),
    ]
