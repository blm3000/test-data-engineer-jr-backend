# Ejercicio práctico para Data Engineer Jr Backend Developer en Deacero.


# Instalación

1. Clonar repositorio a su local
2. Crear un ambiente virtual en su local
3. Ejecutar el comando `pip install -r requirements.txt` para instalar los paquetes necesarios

# Ejecución
Una vez instalados los requerimientos:
- Ejecutar el siguiente comando `python manage.py runserver`\
La instrucción anterior creará un servidor local, con nomenclatura similar a `Starting development server at http://127.0.0.1:8000/`
- Acceder a la dirección generada

- Una vez en la pantalla principal podrá ver el listado de vuelos con sus respectivos usuarios y aerolíneas.
- Podra aplicar un filtro a la tabla por cualquier parámetro que guste
- En la parte de abajo tendrá un botón para agregar una nueva aerolínea


#### Exposición de datos en apis

| Dataset                                    | Api                                                               |
| -------------------------                  | ----------------------------------------------------------------- |
| Lista Pasajeros                            | http://localhost/get-data/pasajeros                               |
| Lista Vuelos                               | http://localhost/get-data/vuelos                                  |
| Lista Aerolineas                           | http://localhost/get-data/aerolineas                              |
| Lista Vuelos-Pasajeros                     | http://localhost/get-data/vuelos-pasajeros                        |
| Lista Aerolíneas-Vuelos-Pasajeros          | http://localhost/get-data/aerolineas-vuelos-pasajeros             |
| Agregar Aerolineas                         | http://localhost/put-data/aerolineas                              |

