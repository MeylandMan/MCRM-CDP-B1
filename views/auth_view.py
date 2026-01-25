import customtkinter as ctk
from tkinter import messagebox

class AuthView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="#eef2ff")
        self.controller = controller
        self.root = root
        self.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        # --- Carte centrale ---
        self.card = ctk.CTkFrame(
            self,
            width=420,
            corner_radius=16,
            fg_color="white"
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # --- Icône ---
        self.icon_frame = ctk.CTkFrame(
            self.card,
            width=60,
            height=60,
            corner_radius=30,
            fg_color="#4f46e5"  # indigo-600
        )
        self.icon_frame.pack(pady=(30, 15))
        self.icon_frame.pack_propagate(False)

        self.icon_label = ctk.CTkLabel(
            self.icon_frame,
            text="🔐",
            text_color="white",
            font=("Arial", 28)
        )
        self.icon_label.pack(expand=True)

        # --- Titre ---
        self.title = ctk.CTkLabel(
            self.card,
            text="Mini CRM",
            font=("Arial", 26, "bold"),
            text_color="#1F2937"
        )
        self.title.pack(pady=(5, 4))

        # --- Sous-titre ---
        self.subtitle = ctk.CTkLabel(
            self.card,
            text="Connectez-vous pour accéder au tableau de bord",
            font=("Arial", 13),
            text_color="#6B7280"
        )
        self.subtitle.pack(pady=(0, 25))

        # --- Formulaire ---
        self.form = ctk.CTkFrame(self.card, fg_color="transparent")
        self.form.pack(padx=30, fill="x")

        # Email
        self.email_label = ctk.CTkLabel(
            self.form,
            text="Email",
            font=("Arial", 12, "bold"),
            text_color="#374151",
            anchor="w"
        )
        self.email_label.pack(fill="x", pady=(0, 6))

        self.email_entry = ctk.CTkEntry(
            self.form,
            placeholder_text="votre@email.com",
            height=40,
            corner_radius=10
        )
        self.email_entry.pack(fill="x", pady=(0, 18))

        # Mot de passe
        self.password_label = ctk.CTkLabel(
            self.form,
            text="Mot de passe",
            font=("Arial", 12, "bold"),
            text_color="#374151",
            anchor="w"
        )
        self.password_label.pack(fill="x", pady=(0, 6))

        self.password_entry = ctk.CTkEntry(
            self.form,
            placeholder_text="••••••••",
            show="•",
            height=40,
            corner_radius=10
        )
        self.password_entry.pack(fill="x", pady=(0, 25))

        # --- Bouton ---
        self.login_button = ctk.CTkButton(
            self.card,
            text="Se connecter",
            height=42,
            corner_radius=10,
            fg_color="#4f46e5",
            hover_color="#4338cA",
            command=self.on_login
        )
        self.login_button.pack(padx=30, fill="x")

        # --- Bloc démo ---
        self.demo_box = ctk.CTkFrame(
            self.card,
            fg_color="#f9fafb",
            corner_radius=12
        )
        self.demo_box.pack(padx=30, pady=25, fill="x")

        self.demo_title = ctk.CTkLabel(
            self.demo_box,
            text="Comptes de démonstration :",
            font=("Arial", 11, "bold"),
            text_color="#4b5563",
            anchor="w"
        )
        self.demo_title.pack(anchor="w", padx=10, pady=(8, 4))

        self.demo_admin = ctk.CTkLabel(
            self.demo_box,
            text="• Admin : admin@example.com / password",
            font=("Arial", 10),
            text_color="#6b7280",
            anchor="w"
        )
        self.demo_admin.pack(anchor="w", padx=10)

        self.demo_commercial = ctk.CTkLabel(
            self.demo_box,
            text="• Commercial : commercial@example.com / password",
            font=("Arial", 10),
            text_color="#6b7280",
            anchor="w"
        )
        self.demo_commercial.pack(anchor="w", padx=10, pady=(0, 8))

    def show_error(self, message: str):
        messagebox.showerror("ERREUR", message)

    def on_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == '' or password == '':
            self.show_error("Veuillez remplir tous les champs.")
            return

        self.controller.login(email, password)


