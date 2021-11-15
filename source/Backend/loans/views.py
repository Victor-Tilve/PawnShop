from django.shortcuts import render, redirect
from .form import CronForm
from .models import TipoPago


def show_tipopago(request):
   form = CronForm()
   
   if request.method == 'POST':
      print(request.POST)
      form = CronForm(request.POST)
      if form.is_valid():
         print('Is valid')
         form.save()
         return redirect('home/')  # 4
      else:  # 5
        # Create an empty form instance
        form = CronForm()
   obj = TipoPago.objects.all().order_by('pk')
   context = {'form': form, 'objects':obj}
   return render(request,'loans/tipopagos.html', context)

def post_list(request):
    return render(request, 'home.html', {})