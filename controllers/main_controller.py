class MainController:
    def __init__(self, root, user, app_controller):
        self.root = root
        self.user = user
        self.app_controller = app_controller

        self.view = None

    def show_dashboard(self):

        # Nettoyer la fenêtre principale
        for widget in self.root.winfo_children():
            widget.destroy()

        from views.main_view import MainView
        self.view = MainView(self.root, self.user["first_name"], self.user["role_user"], self)

        self.root.title("Wemby - Accueil")

    def logout(self):
        self.app_controller.on_logout()

    def get_first_movements(self):
        from models.main_model import MainModel
        return MainModel.get_first_movements()

