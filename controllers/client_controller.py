from views.client_view import ClientView
from models.client_model import ClientModel

class ClientController:
    def __init__(self, content):
        self.content = content
        self.view = None

    def show_clients(self):
        self.view = ClientView(self.content, self)
        self.view.create_widgets()

    def on_new_client(self):
        print("Créer un nouveau client")

    @staticmethod
    def get_clients_count(condition: str):
        return ClientModel.get_client_count(condition)

    @staticmethod
    def get_clients():
        return ClientModel.get_clients()

    @staticmethod
    def get_client(index):
        return ClientModel.get_client(index)

    def add_client(self, company_name, contact_name, email, phone, address, client_statut):
        ClientModel.add_client(company_name, contact_name, email, phone, address, client_statut)