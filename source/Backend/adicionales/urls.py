from django.urls import path
from . import views
urlpatterns = [
path('', views.adicionales_home_view,name='adicionales-home'),
]