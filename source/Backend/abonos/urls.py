from django.urls import path
from . import views
urlpatterns = [
path('', views.abono_home_view),
path('crear/', views.abono_create_view),
path('buscar/', views.abono_search_view),
]