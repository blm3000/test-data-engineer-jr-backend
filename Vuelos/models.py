from django.db import models


class Lineas_Aereas(models.Model):
    """ Se encarga de almancenar Nombres de aerolineas"""

    # Campos
    Code = models.CharField(max_length=200,
                            help_text="Codigo de la aerolinea", unique=True)
    Linea_Aerea = models.CharField(max_length=200,
                                   help_text="Nombre de la aerolinea")

    def __str__(self):
        return self.Linea_Aerea 


class Pasajeros(models.Model):
    """ Se encarga de almancenar informacion de pasajeros"""

    # Campos
    ID_Pasajero = models.IntegerField(
        help_text="Identificador unico del pasajero", unique=True)
    Pasajero = models.CharField(max_length=200, help_text="Nombre del pasajero")
    Edad = models.IntegerField(help_text="Edad actual del pasajero")

    def __str__(self):
        return str(self.ID_Pasajero) + "_" + self.Pasajero


class Vuelos(models.Model):
    """ Se encarga de almancenar vuelos"""

    # Campos
    Viaje = models.DateTimeField(help_text="Fecha del viaje")
    Clase = models.CharField(max_length=20, help_text="Clase del vuelo")
    Precio = models.IntegerField(help_text="Costo del viaje")
    Ruta = models.CharField(max_length=100, help_text="Origen-Destino")

    # Relaciones
    Linea_aerea = models.ForeignKey(
        Lineas_Aereas, to_field="Code",
        null=True, on_delete=models.CASCADE,
        help_text="Referencia a una Lineas_Aereas")
    Pasajero_vuelo = models.ForeignKey(
        Pasajeros, to_field="ID_Pasajero",
        on_delete=models.CASCADE,help_text="Referencia a un pasajero")

    def __str__(self):
        return str(self.Pasajero_vuelo) + "_" + str(self.Viaje)
