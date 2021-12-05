from django.shortcuts import render, redirect
from .form import AbonoForm
from loans.models import Loan
from clients.models import Client
from django.http import JsonResponse
import json

def abono_create_view(request):
    form = AbonoForm()

    if request.method == 'POST':
        print(request.POST)
        form = AbonoForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/')  # 4
        else:  # 5
            # Create an empty form instance
            form = AbonoForm()

    loans = Loan.objects.all().order_by('cliente')
    clientes = Client.objects.all().order_by('nombre')

    context = {
        'form': form,
        'loans': loans,
        'clientes':clientes,
        }
    return render(request, 'abonos/abonos_crear.html', context)


def abono_home_view(request):
    return render(request, 'abonos/abonos_home.html', {})

def abono_search_view(request):
    return render(request, 'abonos/abonos_buscar.html', {})

def check_prestamos_cliente(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        id_cliente = request.GET.get("id_cliente", None)
        loans = Loan.objects.filter(cliente=id_cliente)
        # print (id_cliente)
        # print("-----------------------")
        loans_pk = list(loans.values_list('pk', flat=True).order_by('pk'))
        # print (loans_pk)
        # print (loans.values("interes"))
        # print("-----------------------")
        # print(list(Client.objects.all().filter(pk=id_cliente).values("nombre"))[0]["nombre"])
        # print(list(Client.objects.all().filter(pk=id_cliente).values("nombre"))[0]["nombre"])
        option_loans = []
        for loan in loans_pk:
            option_loans.append(f'<option value="{loan}">{loan}</option>')
        # print(option_loans)
        # results = {loan.pk():{} for loan in loans }
        # for r in search_qs:
        #     results.append(r.FIELD)
        # data = json.dumps(results)
        # # check for the nick name in the database.
        return JsonResponse({"id_loans":option_loans}, status = 200)


    return JsonResponse({}, status = 400)

def check_prestamo_informacion(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        id_prestamo = request.GET.get("id_prestamo", None)
        print(list(Loan.objects.all().filter(pk=id_prestamo).values()))

        prestamo_imformacion = list(Loan.objects.all().filter(pk=id_prestamo).values())
        return JsonResponse({"_prestamo_imformacion":prestamo_imformacion}, status = 200)


    return JsonResponse({}, status = 400)