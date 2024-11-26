from django.urls import path
from urazy import views

urlpatterns = [
    path('', views.urazy_uvod, name="urazy_uvod"),  # Výchozí stránka
    path('detail/', views.urazy_data, name="urazy_data"),  # Detailní stránka bez parametru
]
