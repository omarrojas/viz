from django.urls import path
from eventtia import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tp1', views.tp1, name='tp1'),
    path('ts1_1', views.ts1_1, name='ts1_1'),
    path('ts1_2', views.ts1_2, name='ts1_2'),
    path('tp2', views.tp2, name='tp2'),
    path('ts2_1', views.ts2_1, name='ts2_1'),
    path('ts2_2', views.ts2_2, name='ts2_2'),
    path('tp3', views.tp3, name='tp3'),
    path('ts3_1', views.ts3_1, name='ts3_1'),
    path('ts3_2', views.ts3_2, name='ts3_2'),
    
    ] 