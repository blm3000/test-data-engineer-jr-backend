from django.db import models

# Create your models here.
class Lineas_Aereas(models.Model):
    Code = models.CharField(max_length=200)
    Linea_Aerea = models.CharField(max_length = 200)
    def __str__(self):
        return self.Linea_Aerea 

class Vuelos_2016(models.Model):
    Cve_LA = models.CharField(max_length=10)
    Viaje = models.DateTimeField()
    Clase = models.CharField(max_length=20)
    Precio = models.IntegerField()
    Ruta = models.CharField(max_length=100)
    Cve_Cliente = models.IntegerField()
    def __str__(self):
        return str(self.Cve_Cliente) +"_"+ str(self.Viaje)

class Vuelos_2017(models.Model):
    Cve_LA = models.CharField(max_length=10)
    Viaje = models.DateTimeField()
    Clase = models.CharField(max_length=20)
    Precio = models.IntegerField()
    Ruta = models.CharField(max_length=100)
    Cve_Cliente = models.IntegerField()
    def __str__(self):
        return str(self.Cve_Cliente) +"_"+ str(self.Viaje)

class Pasajeros_2016(models.Model):
    ID_Pasajero = models.IntegerField()
    Pasajero = models.CharField(max_length=200)
    Edad = models.IntegerField()
    def __str__(self):
        return str(self.ID_Pasajero) +"_"+ self.Pasajero

class Pasajeros_2017(models.Model):
    ID_Pasajero = models.IntegerField()
    Pasajero = models.CharField(max_length=200)
    Edad = models.IntegerField()
    def __str__(self):
        return str(self.ID_Pasajero) +"_"+ self.Pasajero