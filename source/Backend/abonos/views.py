from django.shortcuts import render, redirect
from .form import AbonoForm
from loans.models import Loan


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

    context = {
        'form': form,
        'loans': loans,
        }
    return render(request, 'abonos/abonos_crear.html', context)


def abono_home_view(request):
    return render(request, 'abonos/abonos_home.html', {})

def abono_search_view(request):
    return render(request, 'abonos/abonos_buscar.html', {})
