from django.urls import path
from . import views
urlpatterns = [
path('', views.client_home_view, name="clients-home"),
path('crear/', views.client_create_view, name="clients-crear"),
path('buscar/', views.client_search_view, name="clients-buscar"),
]