# Generated by Django 4.1.1 on 2022-10-01 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='fecha_nacimiento',
            new_name='fecha_consulta',
        ),
    ]
