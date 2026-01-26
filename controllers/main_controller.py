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
        user_details = f"{self.user["first_name"]} ({self.user["role_user"]})"
        self.view = MainView(self.root, user_details, self)

        self.root.title("Wemby - Accueil")

    def logout(self):
        self.app_controller.on_logout()

