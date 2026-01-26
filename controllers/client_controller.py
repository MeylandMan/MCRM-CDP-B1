from views.client_view import ClientView


class ClientController:
    def __init__(self, content):
        self.view = ClientView(content, self)

    def show_clients(self):
        self.view.create_widgets()

    def on_new_client(self):
        print("Créer un nouveau client")