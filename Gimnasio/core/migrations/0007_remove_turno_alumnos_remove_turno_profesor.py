# Generated by Django 5.0.6 on 2024-05-14 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_turno_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='alumnos',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='profesor',
        ),
    ]
