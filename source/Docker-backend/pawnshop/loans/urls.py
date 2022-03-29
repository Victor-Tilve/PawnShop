from django.urls import path
from . import views
urlpatterns = [
path('', views.loan_home_view,name='loans-home'),
path('crear/', views.loan_create_view,name='loans-crear'),
path('buscar/', views.loan_search_view,name='loans-buscar'),
path('get/ajax/validate/tabla', views.tabla_prestamo, name = "tabla_prestamo"),
path('cobrarhoy/', views.loan_cobrar_hoy,name='loans-cobrar_hoy'),
path('vencidos/', views.loan_vencidos,name='loans-vencidos'),
path('get/ajax/validate/tabla_cobrar_hoy', views.tabla_cobrar_hoy, name = "tabla_cobrar_hoy"),
]