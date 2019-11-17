from django.shortcuts import render

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

def tp3(request):
    return render(request,'eventtia/tp3.html',{});

def ts3_1(request):
    return render(request,'eventtia/ts3_1.html',{});

def ts3_2(request):
    return render(request,'eventtia/ts3_2.html',{});

def tp2_backend(request):
    resultado = ""
    if request.method == "GET":
        resultado = "hello"
        countryname = request.GET['countryname']
        resultado =  tp2_data(connection, countryname)
#    return resultado
    return render(request,'eventtia/ts3_1.html',{});
 