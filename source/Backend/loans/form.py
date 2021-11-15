from django import forms
from django.forms import ModelForm
from .models import TipoPago

# Crear un nuevo elemento en trabla
class TipoPagoForm(ModelForm):
    class Meta:
        model = TipoPago
        fields = '__all__'

# Desplegar información en drop dawn
class CronForm(forms.Form):
    tipo_de_pago = forms.ModelChoiceField(queryset=TipoPago.objects.all().order_by('tipo'))

