from django.urls import path
from . import views
urlpatterns = [
path('', views.loan_home_view,name='loans-home'),
path('crear/', views.loan_create_view,name='loans-crear'),
path('buscar/', views.loan_search_view,name='loans-buscar'),
path('get/ajax/validate/tabla', views.tabla_prestamo, name = "tabla_prestamo")
]