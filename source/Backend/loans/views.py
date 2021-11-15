from django.shortcuts import render, redirect
from .form import LoanForm
from .models import TipoPago
from clients.models import Client


def create_loan(request):
    form = LoanForm()

    if request.method == 'POST':
        print(request.POST)
        form = LoanForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('home/')  # 4
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
    return render(request, 'loans/_loans.html', context)


def post_list(request):
    return render(request, 'home.html', {})
