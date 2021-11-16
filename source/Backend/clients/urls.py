from django.urls import path
from . import views
urlpatterns = [
path('', views.client_home_view),
path('crear/', views.client_create_view),
path('buscar/', views.client_search_view),
]