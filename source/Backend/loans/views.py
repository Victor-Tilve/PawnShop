from django.shortcuts import render, redirect
from .form import LoanForm
from .models import TipoPago
from clients.models import Client
from .models import Loan


def loan_create_view(request):
    form = LoanForm()

    if request.method == 'POST':
        print(request.POST)
        form = LoanForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/')  # 4
        else:  # 5
            # Create an empty form instance
            form = LoanForm()
    tipo_pagos = TipoPago.objects.all().order_by('pk')
    clientes = Client.objects.all().order_by('nombre')

    context = {
        'form': form,
        'tipo_pagos': tipo_pagos,
        'clientes': clientes,
        }
    return render(request, 'loans/prestamos_crear.html', context)


def loan_home_view(request):
    clientes = Client.objects.all().order_by('pk')
    prestamos = Loan.objects.all().order_by('pk')

    context = {
        'clientes': clientes,
        'prestamos': prestamos,

         }
    return render(request, 'loans/prestamos_home.html', context)

def loan_search_view(request):
    return render(request, 'loans/prestamos_buscar.html', {})
