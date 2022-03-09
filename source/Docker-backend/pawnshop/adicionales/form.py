from django import forms
from django.forms import ModelForm
from .models import Adicional

#TODO: Modificar
class AdicionalForm(ModelForm):
    class Meta:
        model = Adicional
        fields = "__all__"
