import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client: MongoClient = MongoClient(MONGO_URI)

try:
    print("Estableciendo conexión...⏳")
    client.admin.command("ping")
    print("Conexión establecida 😊")
except:
    print("❌ ERROR EN LA CONEXIÓN")
    exit(code=1)

TI3032_U3_EF = client["TI3032_U3_EF"] # Elijo la base de datos

coleccion_clientes = TI3032_U3_EF["clientes"] # Seleccion coleccion Clientes
coleccion_pedidos = TI3032_U3_EF["pedidos"] # Seleccion coleccion Pedidos

def insercion_inicial_coleccion_clientes() -> None:
    respuesta = coleccion_clientes.insert_many(
        [
            {
                "_id": 1,
                "nombre": "Laura Martínez",
                "email": "laura.martinez@gmail.com",
                "fecha_registro": "2026-01-15T10:30:00Z",
                "direccion": "Av. Providencia 1234, Santiago",
                "telefono": "+56 9 8123 4567"
            },
            {
                "_id": 2,
                "nombre": "Carlos Rojas",
                "email": "carlos.rojas@hotmail.com",
                "fecha_registro": "2025-09-22T14:10:00Z",
                "direccion": "Calle Los Aromos 456, Valparaíso",
                "telefono": "+56 9 7234 5678"
            },
            {
                "_id": 3,
                "nombre": "Fernanda Silva",
                "email": "fernanda.silva@gmail.com",
                "fecha_registro": "2024-03-05T09:45:00Z",
                "direccion": "Pasaje Las Rosas 789, Concepción",
                "telefono": "+56 9 6345 6789"
            },
            {
                "_id": 4,
                "nombre": "Javier Torres",
                "email": "javier.torres@outlook.com",
                "fecha_registro": "2026-04-18T16:20:00Z",
                "direccion": "Av. Alemania 321, Temuco",
                "telefono": "+56 9 5456 7890"
            },
            {
                "_id": 5,
                "nombre": "Camila Soto",
                "email": "camila.soto@gmail.com",
                "fecha_registro": "2025-12-02T11:00:00Z",
                "direccion": "Calle San Martín 654, La Serena",
                "telefono": "+56 9 4567 8901"
            },
            {
                "_id": 6,
                "nombre": "Matías Herrera",
                "email": "matias.herrera@yahoo.com",
                "fecha_registro": "2023-07-11T13:25:00Z",
                "direccion": "Av. Brasil 987, Antofagasta",
                "telefono": "+56 9 3678 9012"
            },
            {
                "_id": 7,
                "nombre": "Valentina Fuentes",
                "email": "valentina.fuentes@gmail.com",
                "fecha_registro": "2026-02-28T08:15:00Z",
                "direccion": "Camino El Alba 147, Rancagua",
                "telefono": "+56 9 2789 0123"
            },
            {
                "_id": 8,
                "nombre": "Diego Morales",
                "email": "diego.morales@empresa.cl",
                "fecha_registro": "2022-10-09T17:40:00Z",
                "direccion": "Calle Maipú 258, Talca",
                "telefono": "+56 9 1890 1234"
            },
            {
                "_id": 9,
                "nombre": "Paula Contreras",
                "email": "paula.contreras@gmail.com",
                "fecha_registro": "2025-06-20T12:05:00Z",
                "direccion": "Av. Costanera 369, Puerto Montt",
                "telefono": "+56 9 9001 2345"
            },
            {
                "_id": 10,
                "nombre": "Andrés Vega",
                "email": "andres.vega@icloud.com",
                "fecha_registro": "2024-11-30T15:55:00Z",
                "direccion": "Pasaje Los Pinos 741, Chillán",
                "telefono": "+56 9 8111 2222"
            }
        ]
    )

    print(respuesta)

def insercion_inicial_coleccion_pedidos() -> None:
    pass
