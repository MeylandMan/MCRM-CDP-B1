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
        try:
            user = AuthModel.authenticate(email, password)
            if user:
                print("Connexion réussie pour ", user["first_name"], " (", user["role_user"], ")")
                self.app_controller.on_login_success(user)
            else:
                self.view.show_error("Nom d'utilisateur ou mot de passe incorrect.")
        except Exception as err:
            print("Erreur lors du login : ", err)
            self.view.show_error("Une erreur s'est produite lors de la connexion.")