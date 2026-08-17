from src.sale import Sale

class SalesCollection:
    def __init__(self, sales: list[Sale]):
        self.sales = sales

    def sales_by_client(self, client_id: int):
        sales = []
        for sale in self.sales:
            if sale.client_id == client_id:
                sales.append(sale)

        return sales 

    def total_amount_by_client(self, client_id: int):
        amount = 0
        for sale in self.sales:
            if sale.client_id == client_id:
                amount += sale.amount
        return amount

    def total_amount_by_category(self, category: str):
        amount = 0
        for sale in self.sales:
            if sale.category == category:
                amount += sale.amount
        return amount

    def average_sale_by_client(self, client_id: int):
        total = 0
        contador = 0

        for sale in self.sales:
            if sale.client_id == client_id:
                total += sale.amount
                contador =+ 1

        return total / contador

    