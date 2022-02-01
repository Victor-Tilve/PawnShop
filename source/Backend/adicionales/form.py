from django import forms
from django.forms import ModelForm
from .models import Abono

#TODO: Modificar
class AbonoForm(ModelForm):
    class Meta:
        model = Abono
        fields = "__all__"
