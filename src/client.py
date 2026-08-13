class Client: 
    #Aqui creo mi primera clase: Cliente; con sus atributos, estos atributos los saco del archivo data/clients.json
    def __init__(self, client_id: int, name: str, country: str, signup_date: str):
        self.client_id = client_id
        self.name = name
        self.country = country
        self.signup_date = signup_date

    #Aqui creo el método requerido para convertir el objeto a un diccionario
    def to_dict(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "country": self.country,
            "signup_date": self.signup_date
        }


    