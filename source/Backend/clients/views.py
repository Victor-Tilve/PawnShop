from django.shortcuts import render, redirect
from .form import ClientForm
from .models import Client


def client_create_view(request):
    form = ClientForm()

    if request.method == 'POST':
        print(request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/clients/')  # 4
        else:  # 5
            # Create an empty form instance
            print('Is not valid')
            form = ClientForm()

    context = {
        'form': form,
         }
    return render(request, 'clients/clientes_crear.html', context)


def client_home_view(request):
    clientes = Client.objects.all().order_by('pk')
    context = {
        'clientes': clientes,
         }
    return render(request, 'clients/clientes_home.html', context)

def client_search_view(request):
    return render(request, 'clients/clientes_buscar.html', {})
