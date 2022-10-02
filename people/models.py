from django.db import models

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_consulta = models.DateField(null=True)
    
    def __str__(self):
        return self.persona
