from django.urls import path
from . import views
urlpatterns = [
path('', views.abono_home_view,name='abonos-home'),
path('crear/', views.abono_create_view,name='abonos-crear'),
path('buscar/', views.abono_search_view,name='abonos-buscar'),
path('<int:pk>/', views.AbonosDetailView.as_view(), name='abono_detail'),
path('get/ajax/validate/prestamos_cliente', views.check_prestamos_cliente, name = "check_prestamos_cliente"),
path('get/ajax/validate/prestamo_informacion', views.check_prestamo_informacion, name = "check_prestamo_informacion"),
path('get/ajax/validate/abono_detalle', views.abono_detalle, name = "abono_detalle"),
path('get/ajax/validate/tabla_abono', views.tabla_abono, name = "tabla_abono")
]