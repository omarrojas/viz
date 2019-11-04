from django.shortcuts import render

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