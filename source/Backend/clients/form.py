from django import forms
from django.forms import ModelForm
from .models import Client

# Crear un nuevo elemento en trabla


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
