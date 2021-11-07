from django.contrib import admin

from .models import TipoPago,Loan
admin.site.register(Loan)
admin.site.register(TipoPago)