from src.client import Client

class ClientCollection:
    def __init__(self, clients: list[Client]):
        self.clients = clients

    def get_client_by_id(self, client_id: int):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None


    def clients_by_country(self, country: str):
        # clients = []
        for client in self.clients:
            if client.country == country:
                # return clients.append(client)
                return [client]
        return None