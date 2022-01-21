from django.db.models.fields import Field
from django.shortcuts import render, redirect
from .form import AbonoForm
from loans.models import Loan
from clients.models import Client
from .models import Abono
from django.http import JsonResponse
import json

from django.views.generic import DetailView

def abono_create_view(request):
    form = AbonoForm()

    if request.method == 'POST':
        print(request.POST)
        form = AbonoForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/abonos/')  # 4
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

        prestamo_informacion = list(Loan.objects.all().filter(pk=id_prestamo).values())
        return JsonResponse({"_prestamo_informacion":prestamo_informacion}, status = 200)


    return JsonResponse({}, status = 400)

def tabla_abono(request):
    if request.is_ajax and request.method == "GET":
        tables = []
        abono_table = Abono.objects.values()
        for abonos in abono_table:
            cliente_id = list(Loan.objects.filter(pk=abonos["prestamo_id"]).values())[0]["cliente_id"]
            monto_prestado = list(Loan.objects.filter(pk=abonos["prestamo_id"]).values())[0]["monto_prestado"]
            cliente_nombre = list(Client.objects.filter(pk=cliente_id).values())[0]["nombre"]
            cliente_apellido = list(Client.objects.filter(pk=cliente_id).values())[0]["apellido"]
            tables.append(
                f'<tr><th scope="row">{cliente_id}</th><td>{cliente_nombre}</td><td>{abonos["id"]}</td><td>{monto_prestado}</td><td>{abonos["date_created"]}</td><td>{abonos["abono"]}</td></tr>'
            )
        
        return JsonResponse({"_abonos_imformacion":tables}, status = 200)

        
    return JsonResponse({}, status = 400)


def abono_detalle(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        # print(f'el codigo del prestamo es: {request.GET.get("id_prestamo", None)}')
        id_prestamo = request.GET.get("id_prestamo", None)
                
        prestamo_informacion = list(Loan.objects.all().filter(pk=id_prestamo).values())
        persona_informacion = list(Client.objects.all().filter(pk=prestamo_informacion[0]['cliente_id']).values())
        # print(prestamo_informacion[0])
        # print(persona_informacion[0])
        return JsonResponse({"_prestamo_informacion":prestamo_informacion,"_persona_informacion":persona_informacion}, status = 200)
        


    return JsonResponse({}, status = 400)

class AbonosDetailView(DetailView):
    model = Abono
    template_name = 'abonos/abono_detalle.html'