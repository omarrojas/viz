from django import forms
from .models import tp3edgelist,ts31eventtype

class tp3Form(forms.Form):
    month = forms.ChoiceField(label="Mes a visualizar",choices= tp3edgelist.objects.order_by('month').values_list("month","month").distinct());
    
class ts31Form(forms.Form):
    month = forms.ChoiceField(label="Mes a visualizar",choices= ts31eventtype.objects.order_by('month').values_list("month","month").distinct());