# Ejercicio práctico para Data Engineer Jr Backend Developer en Deacero.

Debe realizar un fork de este repositorio para desarrollar y entregar su trabajo.

Se tiene un requerimiento de análisis de datos de pasajeros, viajes y aerolineas, debemos de proveer APIs para su consumo.
1. Se requiere unificar las listas anuales de vuelos y pasajeros.
2. Las listas obtenidas en el paso anterior y la lista de aerolineas deben de poder accederse mediante una llamada api y con respuesta JSON.
3. Es necesario relacionar las listas de vuelos y pasajeros anteriormente unificadas y hacer una pagina donde se muestre el resultado en formato de libre elección (llamada api JSON, HTML tabla, etc).
4. Los datos obtenidos en el paso anterior se deben relacionar con los datos de las Líneas Aéreas. En caso de no existir la linea aérea catalogarla como otra. El resultado puede mostrarse en formato de libre elección (llamada api JSON, HTML tabla, etc).
5. Se requiere el consumo de datos resultantes filtrados por Linea aerea. El resultado puede mostrarse en formato de libre elección (llamada api JSON, HTML tabla, etc).
6. Por último se pide realizar un mecanismo de captura para registrar una nueva linea aerea a la lista de datos que ya existe. La implementación es a libre elección (llamada api PUT JSON, página HTML, etc).

#### Tip: Esposicion de datos en apis

| Dataset                                    | Api                                                               |
| -------------------------                  | ----------------------------------------------------------------- |
| Lista Pasajeros                            | http://localhost/get-data/pasajeros                               |
| Lista Vuelos                               | http://localhost/get-data/vuelos                                  |
| Lista Aerolineas                           | http://localhost/get-data/aerolineas                              |
| Lista Vuelos-Pasajeros                     | http://localhost/get-data/vuelos-pasajeros                        |
| Lista Aerolíneas-Vuelos-Pasajeros          | http://localhost/get-data/aerolineas-vuelos-pasajeros             |
| Agregar Aerolineas                         | http://localhost/put-data/aerolineas                              |

  Nota: En caso de optar por las apis se propone esta nomenclatura, el api de aerolineas-vuelos-pasajers puede tener un paramtero para el filtrado de datos cuando sea necesario.

Los ejercicios deben realizarse en Django3 - Python3.8 y utilizando el ORM correspondiente, las vistas html pueden realizarse en el mismo framework o mostrarlas de manera nativa o como mejor le convenga. 

Una vez concluido el reto se debe comunicar al correo <jguerrero@deacero.com> con la liga al repositorio de github final para evaluar las respuestas.

Suerte a todos!!! :metal: :nerd_face: :computer:
