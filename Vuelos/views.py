# Archivo views para controlar los direccionamientos de la aplicación "Vuelos"

from django.shortcuts import render, redirect
from Vuelos.models import Lineas_Aereas, Pasajeros, Vuelos  # importamos los modelos


def home(request):
    """ 
        View principal para mostrar todas las aerolienas

        Ruta: /

    """

    vuelos_all = Vuelos.objects.all()
    cols = Vuelos._meta.local_fields

    return render(
        request,
        "Vuelos/home.html",
        {'vuelos': vuelos_all,
         'columnas': cols},
    )


def agregar_aerolinea(request):
    """
        View encargada de agregar una nueva aerolinea	
        Ruta: /vuelos/agregar_aerolinea
    """

    if request.method == 'POST':
        # creamos un nuevo objeto del modelo Lineas_Aereas
        nueva_erolina = Lineas_Aereas()
        # Agregamos atributos
        nueva_erolina.Code = request.POST.get('newCode')
        nueva_erolina.Linea_Aerea = request.POST.get('newNombre')
        nueva_erolina.save()  # lo guardamos

        return redirect("/")
