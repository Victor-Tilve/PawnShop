import this
from django.db import models
import datetime
from datetime import timedelta
# from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator,MaxValueValidator
from clients.models import Client
from django.conf import settings

User = settings.AUTH_USER_MODEL

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

    date_created    = models.DateField()      

    num_cuotas      = models.PositiveIntegerField(validators=[MaxValueValidator(1000)],default=1)

    deadline = models.DateField()
    status = models.BooleanField(default=1) #NOTE: Estado del Prestamo 1 = activo, 2 = Inactivo
    last_modification = models.DateField(default=datetime.date.today)
    creador = models.ForeignKey(User,
                        null = True, 
                        on_delete = models.SET_NULL
                        )
    monto_adeudado   = models.PositiveIntegerField(default=0)
    #TODO: Si se paso de la fecha de pago y el prestamo sigue activo se debe cobrar la cuota mensual en la fecha
    #que corresponda a la decorte. Debo pensar como actualizo la tabla.
    
    #se debe agregar una cuota mas a la lista de fechas si el prestamo aún no s ha cancelado. Cambie de opinion.
    
    #Preguntar a alejandro, si el cliente no paga solo se le capitaliza el interes?
    
    # al seleccionar que x cliente no va a pagar la cuota, se actuliza la fecha de pago a la cuota inmediatamente siguiente
    # a la ultima correspondiente al prestamo y se reaiza un adicional, este adicional puede ser opcional.

    
        
    def __str__(self):
        return f"{self.cliente}: {self.monto_prestado} - {self.date_created}"
    
    class Meta:
        ordering = ('pk',)

class EstadoPago(models.Model):
    '''
    Este modelo es para especificar el estado del pago, de estaforma saber si el pago esta:
    - Pago
    - No pago
    - Incompleto
    '''
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk}: {self.tipo}"
        

class LoanDate(models.Model):
    '''
    Este modelo es para tener el record de los pagos de los clientes y saber las fechas en al que los mismos deben pagar 
    '''
    loan         = models.ForeignKey(Loan, on_delete=models.CASCADE)
    cliente         = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_para_pago    = models.DateField()
    cuota_mensual  =  models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)],default=0)
    status = models.ForeignKey(EstadoPago, on_delete=models.CASCADE)
    
    date_de_pago = models.DateField() #Fecha en que realizaría el pago, que es la misma a la fecha date_para_pago
    retrasado = models.BooleanField(default=0) #NOTE: Sí el pago está retrasado. 1 = verdadero, 2 = falso.

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f"{self.pk}: {self.loan} {self.cliente} {self.date_para_pago}"