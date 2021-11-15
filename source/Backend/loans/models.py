from django.db import models
from datetime import datetime, timedelta
# from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator,MaxValueValidator

from clients.models import Client

def get_deadline(date_created:int,num_meses:int):
    return timedelta(date_created) + timedelta(30*int(num_meses))

# Create your models here.
class TipoPago(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo

class Loan(models.Model):
    cliente         = models.ForeignKey(Client, on_delete=models.CASCADE)
    monto_prestado  =  models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)],default=0)
    interes         = models.FloatField(
                        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],default=0
                    )
    num_meses       = models.PositiveIntegerField(validators=[MaxValueValidator(12)],default=1)
    tipo_pago       = models.ForeignKey(TipoPago, on_delete=models.CASCADE)

    date_created    = models.DateField(auto_now=True)      

    monto_a_pagar   = models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)],default=0)
    num_cuotas      = models.PositiveIntegerField(validators=[MaxValueValidator(1000)],default=1)
    deadline = models.DateField()
    
    def __str__(self):
        return f"{self.cliente}: {self.monto_prestado} - {self.date_created}"
    