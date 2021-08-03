from django.urls import path
from Vuelos import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('vuelos/agregar_aerolinea/', views.agregar_aerolinea,
         name='agregar_aerolinea'),
]