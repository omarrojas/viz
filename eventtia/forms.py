from django import forms
from .models import tp3edgelist,ts31eventtype

class tp3Form(forms.Form):
    #month = forms.ChoiceField(label="Mes a visualizar",choices= tp3edgelist.objects.order_by('month').values_list("month","month").distinct());
    month = forms.ChoiceField(label="Año a visualizar",choices= tp3edgelist.objects.order_by('year').values_list("year","year").distinct());
    
class ts31Form(forms.Form):
    #month = forms.ChoiceField(label="Mes a visualizar",choices= ts31eventtype.objects.order_by('month').values_list("month","month").distinct());
    month = forms.ChoiceField(label="Año a visualizar",choices= ts31eventtype.objects.order_by('year').values_list("year","year").distinct(),widget = forms.Select(attrs = {'onchange' : "submitVIZ();"}));
    email =forms.CharField(label="Email",required=False,widget=forms.TextInput);