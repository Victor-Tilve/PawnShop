from django.db import models
# from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator,MaxValueValidator

from clients.models import Client

# Create your models here.
class TipoPago(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo

class Loan(models.Model):
    cliente         = models.ForeignKey(Client, on_delete=models.CASCADE)
    monto_prestado  =  models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)])
    interes         = models.FloatField(
                        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                    )
    num_meses       = models.PositiveIntegerField(validators=[MaxValueValidator(12)])
    tipo_pago       = models.ForeignKey(TipoPago, on_delete=models.CASCADE)

    def monto_a_pagar(self):
        return self.monto_prestado + (self.monto_prestado * self.interes/100)*self.num_meses
    
    def num_cuotas(self):
        tipo_pago = str(self.tipo_pago)
        if tipo_pago == "Mensual":
            return self.num_meses * 1
        elif tipo_pago == "Quincenal":
            return self.num_meses * 2
        elif tipo_pago == "Semanal":
            return self.num_meses * 4
        elif tipo_pago == "Diario":
            return self.num_meses * 30
        else:
            return None

    date_created    = models.DateTimeField(auto_now=True)          
    
    def __str__(self):
        return f"{self.cliente}: {self.monto_prestado} - {self.date_created}"
    