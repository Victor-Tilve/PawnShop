from django.contrib import admin

from .models import TipoPago,Loan, EstadoPago,LoanDate
admin.site.register(Loan)
admin.site.register(TipoPago)
admin.site.register(EstadoPago)
admin.site.register(LoanDate)