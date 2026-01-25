import customtkinter as ctk

class MainView(ctk.CTkFrame):
    def __init__(self, root, user, controller):
        super().__init__(root)
        self.root = root
        self.user = user
        self.controller = controller

        self.create_layout()

    def create_layout(self):
        pass