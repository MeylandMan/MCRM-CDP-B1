import customtkinter as ctk
from controllers.auth_controller import AuthController
from controllers.main_controller import MainController

class MainApp:
    def __init__(self):
        # Configuration globale Customtkinter
        self.root = ctk.CTk()
        self.root.title("Wemby")
        self.root.geometry("800x600")

        # Initialiser avec l'écran de connexion
        self.auth_controller = AuthController(self.root, self)
        self.auth_controller.show_login_view()

        self.main_controller = None

        self.current_user = None

    def on_login_success(self, user):
        self.current_user = user

        self.main_controller = MainController(self.root, self.current_user, self)
        self.main_controller.show_dashboard()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()