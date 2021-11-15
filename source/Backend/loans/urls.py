from django.urls import path
from . import views
urlpatterns = [
path('', views.show_tipopago),
path('home/', views.post_list),
]