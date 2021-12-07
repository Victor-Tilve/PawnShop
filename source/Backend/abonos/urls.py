from django.urls import path
from . import views
urlpatterns = [
path('', views.abono_home_view,name='abonos-home'),
path('crear/', views.abono_create_view,name='abonos-crear'),
path('buscar/', views.abono_search_view,name='abonos-buscar'),
path('get/ajax/validate/prestamos_cliente', views.check_prestamos_cliente, name = "check_prestamos_cliente"),
path('get/ajax/validate/prestamo_informacion', views.check_prestamo_informacion, name = "check_prestamo_informacion"),
path('get/ajax/validate/tabla_abono', views.tabla_abono, name = "tabla_abono")
]