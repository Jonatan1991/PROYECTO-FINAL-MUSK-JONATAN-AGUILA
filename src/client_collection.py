from client import Client

class Client_collection:
    def __init__(self, clients: list[Client]):
        self.clients = clients

    def get_client_by_id(self, client_id: int):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None


    def clients_by_country(self, country: str):
        for client in self.clients:
            if client.country == country:
                return [client]
        return None