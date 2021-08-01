import json
import sqlite3
from sqlite3 import Error
from datetime import datetime


def create_connection(db_file):
    """ Crea una conexion a la DB
    	
    	ARGS
    		- db_file: String, ruta donde vive la DB
    	
    	Returns
    		- conn: Objeto, conexion a la DB
    		"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

    except Error as e:
        print(e)
    
    return conn


IDs_pasajeros = []
def create_pasajero(conn, pasajero):
    """
    Create registros en la tabla Vuelos de la DB

    ARGS:
    	- conn: Objeto, conexion a la dB
    	- pasajero: Diccionario, Datos para enviar a la DB
    
    Returns:
    	- cur.lastrowid
    """
    global IDs_pasajeros
    sql = ''' INSERT INTO Vuelos_pasajeros(id,ID_Pasajero,Pasajero,Edad)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()

    id_xd = pasajero["pk"]

    if id_xd in IDs_pasajeros:
    	mayor = max(IDs_pasajeros)
    	id_xd = mayor + 1

    ID_Pasajero = pasajero["fields"]["ID_Pasajero"]
    Pasajero = pasajero["fields"]["Pasajero"]
    Edad = pasajero["fields"]["Edad"]

    cur.execute(sql, (id_xd, ID_Pasajero, Pasajero, Edad))
    conn.commit()

    IDs_pasajeros.append(id_xd)

    return cur.lastrowid


IDs_vuelos = []
def create_vuelo(conn, vuelo):
    """
    Create registros en la tabla Vuelos de la DB

    ARGS:
    	- conn: Objeto, conexion a la dB
    	- vuelo: Diccionario, Datos para enviar a la DB
    
    Returns:
    	- cur.lastrowid
    """
    global IDs_vuelos
    sql = ''' INSERT INTO Vuelos_vuelos(id,Viaje,Clase,Precio,Ruta,Linea_aerea_id,Pasajero_vuelo_id)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()

    id_xd = vuelo["pk"]

    if id_xd in IDs_vuelos:
    	mayor = max(IDs_vuelos)
    	id_xd = mayor + 1

    Viaje = datetime.strptime(vuelo["fields"]["Viaje"],"%Y-%m-%dT%H:%M:%SZ")
    Clase = vuelo["fields"]["Clase"]
    Precio = vuelo["fields"]["Precio"]
    Ruta = vuelo["fields"]["Ruta"]
    Linea_aerea_id = vuelo["fields"]["Linea_aerea"]
    if Linea_aerea_id not in ["AA","SW", "AM", "AV", "KL"]:
    	Linea_aerea_id = "OT"

    Pasajero_vuelo_id = vuelo["fields"]["Pasajero_vuelo"]

    cur.execute(sql, (id_xd, Viaje, Clase, Precio, Ruta, Linea_aerea_id, Pasajero_vuelo_id))
    conn.commit()

    IDs_vuelos.append(id_xd)

    return cur.lastrowid


archivo = "/home/psygafas/Documents/DeAcero/test-data-engineer-jr-backend/vuelosFilter.json"
DB = "/home/psygafas/Documents/DeAcero/test-data-engineer-jr-backend/db.sqlite3"
conexion = create_connection(DB)

# Cargamos los datos del JSON
with open(archivo) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

with conexion:
	for objeto in jsonObject:
		if objeto["model"] == "Vuelos.pasajeros":
			print(objeto)
			create_pasajero(conexion, objeto)
		if objeto["model"] == "Vuelos.vuelos":
			print(objeto)
			create_vuelo(conexion, objeto)