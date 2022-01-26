from django.db import models

# from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator,MaxValueValidator

from loans.models import Loan



class Abono(models.Model):
    prestamo        = models.ForeignKey(Loan, on_delete=models.CASCADE)
    abono           = models.PositiveIntegerField(validators=[MaxValueValidator(1000000000)])
    date_created    = models.DateField()          
    
    def __str__(self):
        return f"{self.pk} {self.prestamo}: {self.abono} - {self.date_created}"
    
    class Meta:
        ordering = ('date_created',)