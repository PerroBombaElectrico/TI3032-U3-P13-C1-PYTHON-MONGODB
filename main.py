import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

try:
    print("Estableciendo conexión...⏳")
    client.admin.command("ping")
    print("Conexión establecida 😊")
except:
    print("❌ ERROR EN LA CONEXIÓN")
    exit(code=1)

db_tienda_regex = client["tienda_regex"] # Elijo la base de datos

clientes = db_tienda_regex["clientes"] # Elijo la coleccion

def insercion_inicial_coleccion_clientes() -> None:
    respuesta = clientes.insert_many(
        [
            {
                "nombre": "Ana Torres",
                "email": "ana.torres@gmail.com",
                "ciudad": "Santiago",
                "descripcion": "Cliente frecuente interesada en productos tecnológicos y accesorios."
            },
            {
                "nombre": "Andrés Muñoz",
                "email": "andres.munoz@outlook.com",
                "ciudad": "Valparaíso",
                "descripcion": "Compra notebooks, teclados mecánicos y audífonos gamer."
            },
            {
                "nombre": "Beatriz Rojas",
                "email": "beatriz.rojas@gmail.com",
                "ciudad": "Concepción",
                "descripcion": "Busca ofertas en productos para oficina y escritorio."
            },
            {
                "nombre": "Carlos Pérez",
                "email": "carlos.perez@hotmail.com",
                "ciudad": "La Serena",
                "descripcion": "Cliente nuevo interesado en celulares y planes móviles."
            },
            {
                "nombre": "Camila Soto",
                "email": "camila.soto@duoc.cl",
                "ciudad": "Santiago",
                "descripcion": "Estudiante que compra accesorios para computador."
            },
            {
                "nombre": "Daniela Vargas",
                "email": "daniela.vargas@inacap.cl",
                "ciudad": "Rancagua",
                "descripcion": "Interesada en cursos, tecnología educativa y tablets."
            },
            {
                "nombre": "Diego Herrera",
                "email": "diego.herrera@gmail.com",
                "ciudad": "Temuco",
                "descripcion": "Compra componentes para armar computadores de escritorio."
            },
            {
                "nombre": "Elena Morales",
                "email": "elena.morales@yahoo.com",
                "ciudad": "Antofagasta",
                "descripcion": "Busca productos de seguridad, cámaras y sensores inteligentes."
            },
            {
                "nombre": "Esteban Castro",
                "email": "esteban.castro@outlook.com",
                "ciudad": "Puerto Montt",
                "descripcion": "Cliente interesado en videojuegos, consolas y controles."
            },
            {
                "nombre": "Fernanda Silva",
                "email": "fernanda.silva@gmail.com",
                "ciudad": "Viña del Mar",
                "descripcion": "Compra artículos de oficina, impresoras y tintas."
            },
            {
                "nombre": "Felipe González",
                "email": "felipe.gonzalez@inacap.cl",
                "ciudad": "Santiago",
                "descripcion": "Estudiante interesado en programación, robótica y electrónica."
            },
            {
                "nombre": "Gabriela Fuentes",
                "email": "gabriela.fuentes@hotmail.com",
                "ciudad": "Talca",
                "descripcion": "Prefiere productos económicos para el hogar inteligente."
            },
            {
                "nombre": "Gonzalo Ramírez",
                "email": "gonzalo.ramirez@gmail.com",
                "ciudad": "Iquique",
                "descripcion": "Busca notebooks gamer, monitores y tarjetas gráficas."
            },
            {
                "nombre": "Hugo Medina",
                "email": "hugo.medina@empresa.cl",
                "ciudad": "Santiago",
                "descripcion": "Compra equipos para empresas y soluciones de red."
            },
            {
                "nombre": "Ignacia López",
                "email": "ignacia.lopez@duoc.cl",
                "ciudad": "Chillán",
                "descripcion": "Interesada en tablets, lápices digitales y accesorios."
            },
            {
                "nombre": "Javier Contreras",
                "email": "javier.contreras@gmail.com",
                "ciudad": "Coquimbo",
                "descripcion": "Compra cámaras web, micrófonos y accesorios de streaming."
            },
            {
                "nombre": "Josefa Núñez",
                "email": "josefa.nunez@outlook.com",
                "ciudad": "Santiago",
                "descripcion": "Busca ofertas en celulares, cargadores y audífonos."
            },
            {
                "nombre": "Karina Paredes",
                "email": "karina.paredes@yahoo.com",
                "ciudad": "Arica",
                "descripcion": "Cliente interesada en productos para teletrabajo."
            },
            {
                "nombre": "Luis Fernández",
                "email": "luis.fernandez@empresa.cl",
                "ciudad": "Concepción",
                "descripcion": "Compra routers, switches y dispositivos de conectividad."
            },
            {
                "nombre": "María José Salinas",
                "email": "maria.salinas@gmail.com",
                "ciudad": "Santiago",
                "descripcion": "Busca computadores, monitores y productos de oficina."
            }
        ]
    )

    print(respuesta)

# insercion_inicial_coleccion_clientes()

clientes_documentos = clientes.find()

for documento in clientes_documentos:
    print(
        documento
    )