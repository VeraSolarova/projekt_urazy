from django.urls import path
from urazy import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('vek/', views.vek, name="vek"),  
    path('pohlavi/', views.pohlavi, name="pohlavi"),   
    path('zpusob/', views.zpusob, name="zpusob"), 
    path('pokus/', views.pokus, name="pokus"), 
]