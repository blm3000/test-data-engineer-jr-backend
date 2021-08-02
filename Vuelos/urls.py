from django.urls import path
from Vuelos import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    # path('cuentas/',views.cuentas, name ='Cuentas'),
    # path('agregarPago/',views.agregarPago,name = 'agregarPago'),
    
]