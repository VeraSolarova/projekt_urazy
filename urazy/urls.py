from django.urls import path
from urazy import views

urlpatterns = [
    path('', views.index, name="index"),  # Výchozí stránka
    path('vek/', views.vek, name="vek"),  # Detailní stránka bez parametru
    path('pohlavi/', views.pohlavi, name="pohlavi"),  
    path('vek_graf/', views.vek_graf, name="urazy_graf"),  
    path('zpusob/', views.zpusob, name="zpusob"),  
]

