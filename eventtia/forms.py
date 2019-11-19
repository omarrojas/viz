from django import forms
from .models import tp3edgelist

class tp3Form(forms.Form):
    month = forms.ChoiceField(label="Mes a visualizar",choices= tp3edgelist.objects.order_by('month').values_list("month","month").distinct());