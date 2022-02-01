from django.shortcuts import render, redirect
from .form import LoanForm
from .models import TipoPago
from clients.models import Client
from .models import Loan
from django.http import JsonResponse

def loan_create_view(request):
    form = LoanForm()

    if request.method == 'POST':
        print(request.POST)
        form = LoanForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/loans/')  # 4
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


def tabla_prestamo(request):
    if request.is_ajax and request.method == "GET":
        tables = []
        loans_table = Loan.objects.values()
        for prestamo in loans_table:
            # cliente = list(Client.objects.filter(pk=prestamo.cliente))
            cliente_nombre = list(Client.objects.filter(pk=prestamo["cliente_id"]).values())[0]["nombre"]
            cliente_apellido = list(Client.objects.filter(pk=prestamo["cliente_id"]).values())[0]["apellido"]
            tables.append(
                f'<tr><th scope="row">{prestamo["id"]}</th><td>{prestamo["monto_prestado"]}</td><td>{prestamo["monto_adeudado"]}</td><td>{prestamo["num_meses"]}</td><td>{prestamo["cliente_id"]}</td><td>{cliente_nombre} {cliente_apellido}</td></tr>'
            )
        
        return JsonResponse({"_prestamo_imformacion":tables}, status = 200)

        
    return JsonResponse({}, status = 400)