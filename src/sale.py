class Sale:
    #Clase ventas con sus respectivos atributos
    def __init__(self, sale_id: int, client_id: int, category: str, amount: float, date: str):
        self.sale_id = sale_id
        self.client_id = client_id
        self.category = category
        self.amount = amount
        self.date = date

    #Metodo requerido para convertir el objeto a un diccionario
    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }