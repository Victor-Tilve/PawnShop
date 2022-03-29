from unicodedata import numeric
from django.shortcuts import render, redirect
from .form import LoanForm
from .models import TipoPago, LoanDate,EstadoPago
from clients.models import Client
from .models import Loan
from django.http import JsonResponse
from dateutil.relativedelta import relativedelta


import datetime


def loan_create_view(request):
    form = LoanForm()


    if request.method == 'POST':
        # print(request.POST)
        form = LoanForm(request.POST)
        # cliente = request.POST['cliente']
        # print(f'El cliente es: {cliente}')
        # print(f'el ultimo pk: {lastest_pk.pk}')
        
        # estado_pago = EstadoPago.objects.all().order_by('pk')
        # print(estado_pago)
        
        if form.is_valid():
            print('Is valid')
            form.save()
            
            _loan = Loan.objects.latest('pk')
            _cliente = Client.objects.get(pk=request.POST['cliente']) 
            _num_cuotas = int(request.POST['num_cuotas'])
            _monto_adeudado = request.POST['monto_adeudado']
            _cuota_mensual = float(int(_monto_adeudado)/int(_num_cuotas))
            tipo_pago = request.POST['tipo_pago']
            # retrasado = request.POST['']
            _status = EstadoPago.objects.get(pk='3') 

            print(f'_loan: {_loan}')
            print(f'cuota de: {_cuota_mensual}')
            print(f'Cliente: {_cliente}')

            #estas fechas se deben calcular con un for, teniendo en cuenta el tipo de pago elegido por el cliente
            _date_created = request.POST['date_created']
            _date = _date_created.replace('-', ' ').split(' ')
            _day_date = int(_date[2])
            _month_date = int(_date[1])
            _year_date = int(_date[0])
            _date_created_ = datetime.date(_year_date, _month_date, _day_date)

            for plazo in range(1,_num_cuotas + 1):
                if tipo_pago == '1':
                    _date_para_pago = _date_created_ + relativedelta(months=plazo)
                    loan_date = LoanDate(loan=_loan,
                                         cliente=_cliente,
                                         date_para_pago=_date_para_pago,
                                         cuota_mensual=_cuota_mensual,
                                         status=_status,
                                         date_de_pago = _date_para_pago)

                    loan_date.save()
                    last_loan_date = LoanDate.objects.latest('pk')
                    print(f'Last loan date: {last_loan_date}')
                
                #Verificar funcionamiento
                elif tipo_pago == '2':
                    _date_para_pago = _date_created_ + relativedelta(days=(plazo*15))
                    loan_date = LoanDate(loan=_loan,
                                         cliente=_cliente,
                                         date_para_pago=_date_para_pago,
                                         cuota_mensual=_cuota_mensual,
                                         status=_status,
                                         date_de_pago = _date_para_pago)

                    loan_date.save()
                    last_loan_date = LoanDate.objects.latest('pk')
                    print(f'Last loan date: {last_loan_date}')
                #Verificar funcionamiento
                elif tipo_pago == '3':
                    _date_para_pago = _date_created_ + relativedelta(weeks=plazo)
                    loan_date = LoanDate(loan=_loan,
                                         cliente=_cliente,
                                         date_para_pago=_date_para_pago,
                                         cuota_mensual=_cuota_mensual,
                                         status=_status,
                                         date_de_pago = _date_para_pago)

                    loan_date.save()
                    last_loan_date = LoanDate.objects.latest('pk')
                    print(f'Last loan date: {last_loan_date}')
                #Verificar funcionamiento
                elif tipo_pago == '4':
                    _date_para_pago = _date_created_ + relativedelta(days=(plazo))
                    loan_date = LoanDate(loan=_loan,
                                         cliente=_cliente,
                                         date_para_pago=_date_para_pago,
                                         cuota_mensual=_cuota_mensual,
                                         status=_status,
                                         date_de_pago = _date_para_pago)

                    loan_date.save()
                    last_loan_date = LoanDate.objects.latest('pk')
                    print(f'Last loan date: {last_loan_date}')

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

# Sin finalizar

def loan_cobrar_hoy(request):
    loan_date = LoanDate.objects.all().order_by('pk')
    context = {
    'loan_date': loan_date,
        }
    return render(request, 'loans/prestamos_cobrar_hoy.html',context)

def loan_vencidos(request):
    return render(request, 'loans/prestamos_vencidos.html')

def tabla_cobrar_hoy(request):
    if request.is_ajax and request.method == "GET":
        tables = []
        # fecha_hoy = request.GET.get("fecha_hoy", None)
        #filtra los prestamos que aun estan activos
        _fecha_hoy = request.GET["fecha_hoy"]
        cobrar_hoy_table = LoanDate.objects.filter(date_para_pago=_fecha_hoy,status=EstadoPago.objects.get(pk='3')).values()
        # print(cobrar_hoy_table)
        for cobrar_hoy in cobrar_hoy_table:
            # cliente = list(Client.objects.filter(pk=prestamo.cliente))
            cliente_nombre = list(Client.objects.filter(pk=cobrar_hoy["cliente_id"]).values())[0]["nombre"]
            cliente_apellido = list(Client.objects.filter(pk=cobrar_hoy["cliente_id"]).values())[0]["apellido"]
            # print(cliente_nombre)
            tables.append(
                f'<tr><th scope="row">{cobrar_hoy["id"]}</th><td>{cobrar_hoy["loan_id"]}</td><td>{cobrar_hoy["date_para_pago"]}</td><td>{cobrar_hoy["cuota_mensual"]}</td><td>{cobrar_hoy["cliente_id"]}</td><td>{cliente_nombre} {cliente_apellido}</td></tr>'
            )

        # print(tables)
        
        return JsonResponse({"table_loan_date":tables}, status = 200)

        
    return JsonResponse({}, status = 400)
