from django.shortcuts import render, redirect
from .form import ClientForm



def client_create_view(request):
    form = ClientForm()

    if request.method == 'POST':
        print(request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            print('Is valid')
            form.save()
            return redirect('/')  # 4
        else:  # 5
            # Create an empty form instance
            form = ClientForm()

    context = {
        'form': form,
         }
    return render(request, 'clients/clientes_crear.html', context)


def client_home_view(request):
    return render(request, 'clients/clientes_home.html', {})

def client_search_view(request):
    return render(request, 'clients/clientes_buscar.html', {})
