import json
import pandas as pd

from src.client import Client
from src.client_collection import ClientCollection

from src.sale import Sale
from src.sales_collection import SalesCollection

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

    sales_objects = []
    sales_df = pd.read_csv(ruta_sales)

    

    for col, row in sales_df.iterrows():
        sale = Sale(
            sale_id=row['sale_id'],
            client_id=int(row['client_id']),
            product=row['product'],
            category=row['category'],
            amount=float(row['amount']),
            date=row['date']
        )
        sales_objects.append(sale)

    sales_collection = SalesCollection(sales_objects)

    # Segundo cálculo
    total_ventas = len(sales_collection.sales)

    # suba de todas las ventas
    total_revenue = round(sales_collection.total_revenue(), 2)

    clients_list = []
    for client in collection_client.clients:
         # 3) Total gastado por cliente
        total_spent = sales_collection.total_amount_by_client(client.client_id)
        
        # 4) Cantidad de ventas por cliente
        sales_by_c = sales_collection.sales_by_client(client.client_id)
        sale_count = len(sales_by_c)
        
        # 5) Promedio de gasto por este cliente (redondeado a 2 decimales)
        average_sale = 0.0
        if sale_count > 0:
            average_sale = round(sales_collection.average_sale_by_client(client.client_id), 2)

        # Agregamos la información en el formato esperado por los tests
        clients_list.append({
            "client_id": client.client_id,
            "name": client.name,
            "country": client.country,
            "signup_date": client.signup_date,
            "total_spent": total_spent,
            "sale_count": sale_count,
            "average_sale": average_sale
        })

    # Calculo numero 6
    # Creo 2 disccionarios uno para el pais y el gasto para buscar cual es el myor y el otro para agrupar el cliente y el pais
    top_client_by_country = {}
    max_spent_by_country = {}
    # Luego recorro la lista de cklientes creada anteriormente
    for client in clients_list:
        #creo las variables que me hacne flata, pais, nombre y gasto para luego usarlas
        pais = client["country"]
        nombre = client["name"]
        gasto = client["total_spent"]
        # aqui creo la condicion que me permite saber cual es el gasto mayor para agregarlos al diccionario por orden
        if pais not in max_spent_by_country or gasto > max_spent_by_country[pais]:
            max_spent_by_country[pais] = gasto
            top_client_by_country[pais] = nombre

    report = {
        "summary": {
            "total_clients": total_clientes,
            "total_sales": total_ventas,
            "total_revenue": total_revenue
        }, 
        "clients": clients_list,
        "top_client_by_country": top_client_by_country
    }

    return report

print("--- Probando el primer y segundo cálculo ---")
resultado = generate_report()
print(resultado)
