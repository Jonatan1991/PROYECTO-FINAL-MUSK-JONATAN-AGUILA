import json
import pandas as pd
from src.client import Client
from src.client_collection import ClientCollection

def generate_report():


    ruta_client = "data/clients.json"
    ruta_sales = "data/sales.csv"

    with open(ruta_client, 'r', encoding='utf-8') as file:
        clients_data = json.load(file)

   


    #convierto el json en un objeto
    client_object = []
    for c in clients_data:
        client = Client(
            client_id=c['client_id'],
            name=c['name'],
            country=c['country'],
            signup_date=c['signup_date']
        )
        client_object.append(client)

    #Ahora client_collection lo tengo para guardar la lista de clientes y trabajar con ella, entonces guardo los clientes ahi
    collection_client = ClientCollection(client_object)

    #Primer Calculo
    total_clientes = len(collection_client.clients)

    report = {
        "summary": {
            "total_clients": total_clientes,
            "total_sales": 0,        # De momento en 0, lo calcularás en el siguiente paso
            "total_revenue": 0.0
        }
    }

    return report

print("--- Probando nuestro primer cálculo ---")
resultado = generate_report()
print(resultado)