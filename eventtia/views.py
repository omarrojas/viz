from django.shortcuts import render
from django.http import HttpResponse

from .vtp2 import tp2_data

# Común para el acceso a la BD
import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('db.sqlite3')
connection.row_factory = dict_factory

# Create your views here.

def index(request):
    return render(request,'eventtia/index.html',{});

def tp1(request):
    return render(request,'eventtia/tp1.html',{});

def ts1_1(request):
    return render(request,'eventtia/ts1_1.html',{});

def ts1_2(request):
    return render(request,'eventtia/ts1_2.html',{});

def tp2(request):
    return render(request,'eventtia/tp2.html',{});

def ts2_1(request):
    return render(request,'eventtia/ts2_1.html',{});

def ts2_2(request):
    return render(request,'eventtia/ts2_2.html',{});


from .models import tp3edgelist
from .forms import tp3Form
def tp3(request):
    if request.method == 'POST':
        
        form = tp3Form(request.POST);
        
        if form.is_valid():
            
            month = form.cleaned_data['month'];
            print('Mes a buscar', month);
        
        
            edgelist_T = list(tp3edgelist.objects.filter(month=month));
            print('edgelist_T',edgelist_T);
            
            edgelist=[];
            for i in edgelist_T:
                object = {
                    "source":i.source,
                    "target":i.target,
                    "weight":i.weight,            
                    }
                edgelist.append(object);
            print('edgelist',edgelist);
            
            nodelist_S= list(tp3edgelist.objects.values('source').filter(month=month).distinct());
            print('nodelist_S',nodelist_S);
            nodelist_T= list(tp3edgelist.objects.values('target').filter(month=month).distinct());
            print('nodelist_T',nodelist_T);
            
            nodelist=[];
            for i in nodelist_S:
                object = {
                    "id":i['source'],
                    "role":"evento"
                    }
                nodelist.append(object);
            
            for i in nodelist_T:
                object = {
                    "id":i['target'],
                    "role":"participante"
                    }
                nodelist.append(object);
            
            
            
            print('nodelist',nodelist)
            
            return render(request,'eventtia/tp3.html',{"edgelist":edgelist,"nodelist":nodelist,"buscado":month,'formset': form});
        else:
            print(form)
    else:
        formset = tp3Form()
        return render(request, 'eventtia/tp3.html', {'formset': formset});

    

from .models import ts31eventtype
from .forms import ts31Form
from django.db.models import Count
def ts3_1(request):
    if request.method == 'POST':
        
        form = tp3Form(request.POST);
        
        if form.is_valid():
            
            month = form.cleaned_data['month'];
            print('Mes a buscar', month);
            
            countType = list(ts31eventtype.objects.filter(month=month).values('type').annotate(count=Count('type')));
            #list(ts31eventtype.objects.values('type').annotate(count=Count('type')));
            print('ts3.1',countType);
            
            nodelist=[];
            for i in countType:        
                object = {
                    "Name":i['type'],
                    "Count":i['count']
                    }
                nodelist.append(object);
            
            countTypeList = {"children":nodelist};
            
            return render(request,'eventtia/ts3_1.html',{'countTypelist':countTypeList,"buscado":month,'formset': form});
        else:
            print(form)
    else:
        formset = ts31Form()
        return render(request, 'eventtia/ts3_1.html', {'formset': formset});

def ts3_2(request):
    return render(request,'eventtia/ts3_2.html',{});

def tp2_backend(request):
    resultado = ""
    if request.method == "GET":
        resultado = "hello"
        countryname = request.GET['countryname']
        resultado =  tp2_data(connection, countryname)
#    return resultado
    return HttpResponse(resultado, content_type='application/json')
    #return render(request,'eventtia/ts3_1.html',{});
 