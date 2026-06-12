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

    )

    print(respuesta)

def insercion_inicial_coleccion_pedidos() -> None:
    pass