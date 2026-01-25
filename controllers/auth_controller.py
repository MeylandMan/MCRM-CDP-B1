class AuthController:
    def __init__(self, root, app_controller):
        self.root = root
        self.app_controller = app_controller
        self.view = None

    def show_login_view(self):
        from views.auth_view import AuthView

        # Nettoyer la fenêtre principale
        for widget in self.root.winfo_children():
            widget.destroy()

        self.view = AuthView(self.root, self)
        self.root.title("Wemby - Connexion")

    def login(self, email, password):
        from models.auth_model import AuthModel
        user = AuthModel.authenticate(email, password)

        if user:
            print("Connected successfully")
        else:
            print("The user does not exist")