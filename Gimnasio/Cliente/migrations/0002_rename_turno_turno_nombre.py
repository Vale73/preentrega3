# Generated by Django 5.0.6 on 2024-05-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='turno',
            new_name='nombre',
        ),
    ]
