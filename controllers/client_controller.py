from views.client_view import ClientView


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
        from models.client_model import ClientModel
        return ClientModel.get_client_count(condition)