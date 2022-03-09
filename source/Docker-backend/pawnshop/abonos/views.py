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
        # print(request.POST)
        allpost = request.POST
        form = AbonoForm(request.POST)
        if form.is_valid():
            # print('Is valid')
            
            #----------
            id_prestamo = allpost.get("prestamo", None)
            # print(f"El id del prestamo: {id_prestamo}")
            abono = allpost.get("abono", None)
            # print(f"El abono es: {abono}")
            # adeudado = Loan.objects.filter(pk=id_prestamo)
            adeudado = list(Loan.objects.filter(pk=id_prestamo).values())[0]["monto_adeudado"]
            # print(f"Valor de deuda: {adeudado}")
            # print(f"tipo de dato: {type(adeudado)}")
            new_adeudado = int(adeudado) - int(abono)
            Loan.objects.filter(pk=id_prestamo).update(monto_adeudado=new_adeudado)
            # _adeudado = list(Loan.objects.filter(pk=id_prestamo).values())[0]["monto_adeudado"]
            # print(f"Valor del deuda a actualizar: {_adeudado}")

            #TODO: si el abono hace que el dinero pagado sea menor o igual a 0, desactivar prestamo
            #TODO: Si el el unico prestamo que tenía activo, desactivar Cliente

            #----------
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
    #Metodo para verificar todos los prestamos asociados a un cliente. se utilizan solo los pk de los prestamos 
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        id_cliente = request.GET.get("id_cliente", None)
        # print ("check_prestamos_cliente:El cliente es" + str(id_cliente))
        loans = Loan.objects.filter(cliente=id_cliente)
        # print ("check_prestamos_cliente:Los prestamos son" + str(loans))
        
        option_loans = []
        if len(loans) > 0:
            # print("check_prestamos_cliente:Dentro del condicional")
            loans_pk = list(loans.values_list('pk', flat=True).order_by('pk'))
            for loan in loans_pk:
                option_loans.append(f'<option value="{loan}">{loan}</option>')
        else:
            # print("check_prestamos_cliente:Dentro del Else")
            option_loans.append(f'<option value="">---------</option>')
            return JsonResponse({"id_loans":option_loans}, status = 200)
        # print(option_loans)
        # results = {loan.pk():{} for loan in loans }
        # for r in search_qs:
        #     results.append(r.FIELD)
        # data = json.dumps(results)
        # # check for the nick name in the database.
        return JsonResponse({"id_loans":option_loans}, status = 200)


    return JsonResponse({}, status = 400)

# Metodo utlizado al momento de Crear un nuevo abono. toma el valor del prestamo y complementa el resto de informacióń del mismo
def check_prestamo_informacion(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        id_prestamo = request.GET.get("id_prestamo", None)
        # print("check_prestamo_informacion: Dentro")
        # print ("check_prestamo_informacion: Id prestamo" + str(id_prestamo))
        if id_prestamo != "":
            abono_informacion = list(Abono.objects.all().filter(prestamo=id_prestamo).values())
            #If abono_informacion is empty
            #if there are more than one, pick the last one
            #Else, un solo dato
            if len(abono_informacion) == 0:
                abono_informacion = [{'abono': 0,'date_created': "mm/dd/yyyy"}]
            elif len(abono_informacion) > 1:
                abono_informacion = [abono_informacion[-1]]

            prestamo_informacion = list(Loan.objects.all().filter(pk=id_prestamo).values())
            return JsonResponse({"_prestamo_informacion":prestamo_informacion,"_abono_informacion":abono_informacion}, status = 200)
        else:
            return JsonResponse({"_prestamo_informacion":"---------","_abono_informacion":"---------"}, status = 200)


    return JsonResponse({}, status = 400)

def tabla_abono(request):
    if request.is_ajax and request.method == "GET":
        tables = []
        abono_table = Abono.objects.values()
        for abonos in abono_table:
            cliente_id = list(Loan.objects.filter(pk=abonos["prestamo_id"]).values())[0]["cliente_id"]
            monto_adeudado = list(Loan.objects.filter(pk=abonos["prestamo_id"]).values())[0]["monto_adeudado"]
            cliente_nombre = list(Client.objects.filter(pk=cliente_id).values())[0]["nombre"]
            cliente_apellido = list(Client.objects.filter(pk=cliente_id).values())[0]["apellido"]
            tables.append(
                f'<tr><th scope="row">{cliente_id}</th><td>{cliente_nombre} {cliente_apellido}</td><td>{abonos["id"]}</td><td>{monto_adeudado}</td><td>{abonos["date_created"]}</td><td>{abonos["abono"]}</td></tr>'
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

##COMEBACK: NO Recuerdo en donde estoy utilizando
class AbonosDetailView(DetailView):
    model = Abono
    template_name = 'abonos/abono_detalle.html'