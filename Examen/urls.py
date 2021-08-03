"""Examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from Vuelos import resources
from tastypie.api import Api

# Creamos una instancia de la Para poder utilizar la API
get_data = Api(api_name='get-data')
get_data.register(resources.PasajerosRecurso())
get_data.register(resources.VuelosRecurso())
get_data.register(resources.AerolineasRecurso())
get_data.register(resources.VuelosPasajerosRecurso())
get_data.register(resources.AereoVueloPasajero())


put_data = Api(api_name='put-data')
put_data.register(resources.AerolineasPut())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vuelos.urls')),
    path('', include(get_data.urls)),
    path('', include(put_data.urls)),
]
