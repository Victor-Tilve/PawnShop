from django import forms
from django.forms import ModelForm
from .models import TipoPago, Loan,LoanDate

# Crear un nuevo elemento en trabla


class LoanForm(ModelForm):
    class Meta:
        model = Loan
        # fields = "__all__"
        # Aquí están todas, verificar cuales no hacen falta
        fields = [
            'cliente',
            'monto_prestado',
            'interes',
            'num_meses',
            'tipo_pago',
            'date_created',
            'num_cuotas',
            'deadline',
            'creador', #new
            'monto_adeudado', #new
        ]
# <QueryDict: {'csrfmiddlewaretoken': ['uO21R3ZDbgHBIrd3waiRW2cf1NSxNrF8sXloltarHjaE93JtVwNWArWkNNjdwg4E'], 'creador': ['vats'], 'monto_adeudado': ['100'], 'cliente': ['1'], 'date_created': ['2022-01-30'], 'monto_prestado': ['0100'], 'interes': ['10'], 'num_meses': ['2'], 'tipo_pago': ['1'], 'monto_a_pagar': ['120'], 'num_cuotas': ['2'], 'deadline': ['2022-03-30'], 'save': ['']}>
# Desplegar información en drop dawn


class CronForm(forms.Form):
    tipo_de_pago = forms.ModelChoiceField(
        queryset=TipoPago.objects.all().order_by('tipo'))

class LoanDateForm(ModelForm):
    class Meta:
        model = LoanDate
        fields = [
            'loan',
            'cliente',
            'date_para_pago',
            'cuota_mensual',
            'status',
            'date_de_pago',
            'retrasado',
        ]