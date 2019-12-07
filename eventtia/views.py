from django.shortcuts import render
from django.http import HttpResponse

from .vtp2 import tp2_data
from .vts2_1 import ts2_1_data
from .vts2_2 import ts2_2_data

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
from django.db.models import Count
from .forms import tp3Form
def tp3(request):
    if request.method == 'POST':
        
        form = tp3Form(request.POST);
        
        if form.is_valid():
            
            month = form.cleaned_data['month'];
            
            amountEven = request.POST['rangeVal'];
            
            print('Año a buscar', month, "CantidadEventos=",amountEven);
        
        
            distlist_T = tp3edgelist.objects.filter(year=month).values('target').distinct().annotate(cant=Count('target')).filter(cant__gt=amountEven).values('target')[:100]


            edgelist_T = list(tp3edgelist.objects.filter(year=month, target__in=distlist_T));
            #print('edgelist_T',edgelist_T);
            
            edgelist=[];
            for i in edgelist_T:
                object = {
                    "source":i.source,
                    "target":i.target,
                    "weight":i.weight,       
                    }
                edgelist.append(object);
            #print('edgelist',edgelist);
            
            nodelist_S= list(tp3edgelist.objects.values('source','type').order_by('source').filter(year=month, target__in=distlist_T).distinct())[:45];
            #print('nodelist_S',nodelist_S);
            nodelist_T= list(tp3edgelist.objects.values('target').order_by('target').filter(year=month, target__in=distlist_T).distinct());
            #print('nodelist_T',nodelist_T);
            
            nodelist=[];
            for i in nodelist_S:
                object = {
                    "id":i['source'],
                    "role":"evento",                    
                    "type":i['type'],     
                    }
                nodelist.append(object);
            
            for i in nodelist_T:
                object = {
                    "id":i['target'],
                    "role":"participante",
                    }
                nodelist.append(object);
            
            sizeX_VIZ= (len(nodelist_T) * 17) + 150
            
            #print('nodelist',nodelist)
            
            return render(request,'eventtia/tp3.html',{"edgelist":edgelist,"nodelist":nodelist,"buscado":month,"amountEven":amountEven,"sizeX_VIZ":sizeX_VIZ,'formset': form});
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
        
        form = ts31Form(request.POST);
        
        if form.is_valid():            
            
            month =  form.cleaned_data['month']
            email = form.cleaned_data["email"]
            
            print('Año a buscar', month, 'email',email);
            
            if(email == ""):
                countType = list(ts31eventtype.objects.filter(year=month).values('type').annotate(count=Count('type')));                
            else:
                countType = list(tp3edgelist.objects.filter(year=month,target=email).values('type').annotate(count=Count('type')));
                            
                        
            nodelist=[];
            for i in countType:        
                object = {
                    "Name":i['type'],
                    "Count":i['count']
                    }
                nodelist.append(object);
            
            countTypeList = {"children":nodelist};
            #print('ts3.1',countTypeList);
            
            return render(request,'eventtia/ts3_1.html',{'countTypelist':countTypeList,"buscado":month,'formset': form});
        else:
            print(form)
    else:
        formset = ts31Form()
        return render(request, 'eventtia/ts3_1.html', {'formset': formset});

def ts3_2(request):
    return render(request,'eventtia/ts3_2.html',{});

# Backend endpoints
def tp2_backend(request):
    resultado = ""
    if request.method == "GET":
        resultado = "hello"
        countryname = request.GET['countryname']
        weekday = request.GET['weekday']
        resultado =  tp2_data(connection, countryname, weekday)
    return HttpResponse(resultado, content_type='application/json')

def ts2_1_backend(request):
    resultado = ""
    if request.method == "GET":
        resultado = "hello"
        attendeetypename = request.GET['attendeetypename']
        resultado =  ts2_1_data(connection, attendeetypename, )
    return HttpResponse(resultado, content_type='application/json')

def ts2_2_backend(request):
    resultado = ""
    if request.method == "GET":
        resultado = "hello"
        countryname = request.GET['countryname']
        weekday = request.GET['weekday']
        resultado =  ts2_2_data(connection, countryname, weekday)
    return HttpResponse(resultado, content_type='application/json')
