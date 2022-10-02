from django.db import models

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Nrofav = models.IntegerField()
    fecha_nac = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.nombre}{self.apellido}"
