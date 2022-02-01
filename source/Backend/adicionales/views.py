from django.shortcuts import render

# Create your views here.
def adicionales_home_view(request):
    return render(request, 'adicionales/adicionales_home.html', {})