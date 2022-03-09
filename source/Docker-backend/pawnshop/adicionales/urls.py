from django.urls import path
from . import views
urlpatterns = [
path('', views.adicionales_home_view,name='adicionales-home'),
path('crear/', views.adicionales_create_view,name='adicionales-crear'),
path('buscar/', views.adicionales_search_view,name='adicionales-buscar'),
path('get/ajax/validate/tabla_adicionales', views.tabla_adicionales, name = "tabla_adicionales"),
]