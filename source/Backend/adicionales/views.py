from django.shortcuts import render
from .form import AdicionalForm
from loans.models import Loan
from clients.models import Client
from .models import Adicional
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def adicionales_home_view(request):
    return render(request, 'adicionales/adicionales_home.html', {})

def adicionales_create_view(request):
    form = AdicionalForm()

    if request.method == 'POST':
        # print(request.POST)
        allpost = request.POST
        form = AdicionalForm(request.POST)
        if form.is_valid():
            # print('Is valid')
            
            #----------
            id_prestamo = allpost.get("prestamo", None)
            print(f"El id del prestamo: {id_prestamo}")
            adicional = allpost.get("adicional", None)
            print(f"El adicional es: {adicional}")
            
            adeudado = list(Loan.objects.filter(pk=id_prestamo).values())[0]["monto_adeudado"]
            print(f"Valor de deuda: {adeudado}")
            # print(f"tipo de dato: {type(adeudado)}")
            new_adeudado = int(adeudado) + int(adicional)
            Loan.objects.filter(pk=id_prestamo).update(monto_adeudado=new_adeudado)
            _adeudado = list(Loan.objects.filter(pk=id_prestamo).values())[0]["monto_adeudado"]
            print(f"Valor del deuda a actualizar: {_adeudado}")

            #----------
            form.save()
            return redirect('/adicionales/')  # 4
        else:  # 5
            # Create an empty form instance
            form = AdicionalForm()

    loans = Loan.objects.all().order_by('cliente')
    clientes = Client.objects.all().order_by('nombre')

    context = {
        'form': form,
        'loans': loans,
        'clientes':clientes,
        }
    return render(request, 'adicionales/adicionales_crear.html', context)

def adicionales_search_view(request):
    return render(request, 'adicionales/adicionales_buscar.html', {})

def tabla_adicionales(request):
    if request.is_ajax and request.method == "GET":
        tables = []
        adicional_table = Adicional.objects.values()
        for adicional in adicional_table:
            cliente_id = list(Loan.objects.filter(pk=adicional["prestamo_id"]).values())[0]["cliente_id"]
            monto_adeudado = list(Loan.objects.filter(pk=adicional["prestamo_id"]).values())[0]["monto_adeudado"]
            cliente_nombre = list(Client.objects.filter(pk=cliente_id).values())[0]["nombre"]
            cliente_apellido = list(Client.objects.filter(pk=cliente_id).values())[0]["apellido"]
            tables.append(
                f'<tr><th scope="row">{cliente_id}</th><td>{cliente_nombre} {cliente_apellido}</td><td>{adicional["id"]}</td><td>{monto_adeudado}</td><td>{adicional["date_created"]}</td><td>{adicional["adicional"]}</td></tr>'
            )
        
        return JsonResponse({"_adicionales_informacion":tables}, status = 200)

        
    return JsonResponse({}, status = 400)

