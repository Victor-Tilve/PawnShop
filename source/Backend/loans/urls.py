from django.urls import path
from . import views
urlpatterns = [
path('', views.loan_home_view),
path('crear/', views.loan_create_view),
path('buscar/', views.loan_search_view),
]