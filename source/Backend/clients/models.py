from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    nombre = models.CharField(max_length=200,null=False)
    apellido = models.CharField(max_length=200,null=False)
    cedula = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],null=False)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')],null=False)
    direccion = models.CharField(max_length=200,null=False)
    direccion2 = models.CharField(max_length=200,blank=True)

    ref1 = models.CharField(max_length=200,blank=True)
    telefono_ref1 = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
             
    def __str__(self):
        return f"{self.nombre} {self.apellido}"