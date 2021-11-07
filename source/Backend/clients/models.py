from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    direccion = models.CharField(max_length=200)
    direccion2 = models.CharField(max_length=200)

    ref1 = models.CharField(max_length=200)
    telefono_ref1 = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
             
    def __str__(self):
        return f"{self.nombre} {self.apellido}"