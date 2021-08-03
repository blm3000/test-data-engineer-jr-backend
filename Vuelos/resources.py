# Vuelos/ resources.py
# librerias necesarias para hacer uso de la api
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from Vuelos.models import Lineas_Aereas, Pasajeros, Vuelos


# Clase que sevirá para mostrar los resultados de todos
# los registros de Pasajeros
class PasajerosRecurso(ModelResource):
    class Meta:
        queryset = Pasajeros.objects.all()
        resource_name = 'pasajeros'


# Clase que sevirá para mostrar los resultados de todos
# los registros de Aerolineas
class AerolineasRecurso(ModelResource):
    class Meta:
        queryset = Lineas_Aereas.objects.all()
        resource_name = 'aerolineas'


# Clase que sevira para mostrar los resultados de todos los registros de Vuelos
class VuelosRecurso(ModelResource):
    # HAcemos referencia al recurso creado para ver el pasajero y aerolinea
    # Full = True, nos trae los datos, si queremos que nos traiga la
    # url del pasajero o vuelo
    # lo ponemos en False
    Pasajero_vuelo = fields.ForeignKey(
        PasajerosRecurso,
        attribute='Pasajero_vuelo', null=True, full=True)

    Linea_aerea = fields.ForeignKey(
        AerolineasRecurso,
        attribute='Linea_aerea', null=True, full=True)

    class Meta:
        queryset = Vuelos.objects.all()
        resource_name = 'vuelos'


# Clase que sevirá para mostrar los resultados de todos los registros
# de Vuelos con pasajeros
class VuelosPasajerosRecurso(ModelResource):
    Pasajero_vuelo = fields.ForeignKey(
        PasajerosRecurso,
        attribute='Pasajero_vuelo', null=True, full=True)
    class Meta:
        queryset = Vuelos.objects.all().\
            only("Viaje", "Clase", "Precio", "Ruta", "Pasajero_vuelo")
        resource_name = 'vuelos-pasajeros'


# Clase que sevirá para mostrar los resultados de todos los registros de Vuelos
class AereoVueloPasajero(ModelResource):
    # HAcemos referencia al recurso creado para ver el pasajero y aerolinea
    # Full = True, nos trae los datos, si queremos que nos traiga
    # la url del pasajero o vuelo
    # lo ponemos en False
    Pasajero_vuelo = fields.ForeignKey(
        PasajerosRecurso,
        attribute='Pasajero_vuelo', null=True, full=True)
    Linea_aerea = fields.ForeignKey(
        AerolineasRecurso,
        attribute='Linea_aerea', null=True, full=True)
    class Meta:
        queryset = Vuelos.objects.all()
        resource_name = 'aerolineas-vuelos-pasajeros'

        # Aplicamos un filtrado, en este caso estamos diciendo que se pueda filtrar
        # Por El atributo clase, podria ser cualquiera de los atributos del objeto
        filtering = {
            "slug": ('exact', 'startswith',),
            "Clase": ALL,
        }


# Clase que sevirá para cargar datos a Aerolineas
class AerolineasPut(ModelResource):
    class Meta:
        queryset = Lineas_Aereas.objects.all()
        resource_name = 'aerolineas'

        # Por default solo se permiten opeaciones GET, para hacer POST o PUT
        # Debemos configurar algunas cosas de autorizacion
        authorization = Authorization()
