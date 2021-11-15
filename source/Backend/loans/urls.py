from django.urls import path
from . import views
urlpatterns = [
path('', views.create_loan),
path('home/', views.post_list),
]