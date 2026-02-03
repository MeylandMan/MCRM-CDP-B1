import customtkinter as ctk


def show_delete_user_panel(index, view):
    from tkinter import messagebox
    response = messagebox.askquestion("Delete confirmation", "Voulez vous VRAIMENT supprimer cet utilisateur ?")

    if response == "yes":
        from controllers.user_controller import UserController
        UserController.delete_user(index)
        view.refresh_widgets()


class UserView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller
        self.search_value = None

        self.pack(fill="both", expand=True)

    def refresh_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

    def create_widgets(self):
        # -----------------------------
        # Mock users
        # -----------------------------
        users = self.controller.get_users(self.search_value)

        # -----------------------------
        # Header
        # -----------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        left = ctk.CTkFrame(header, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkLabel(
            left,
            text="Utilisateurs",
            font=("Arial", 22, "bold"),
            text_color="#111827"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text=f"{len(users)} utilisateurs au total",
            font=("Arial", 12),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="+ Nouveau utilisateur",
            fg_color="#4f46e5",
            height=38,
            corner_radius=8,
            command=lambda: self.show_user_form("Creer", -1)
        ).pack(side="right")

        # -----------------------------
        # Search bar
        # -----------------------------
        search_card = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search_card.pack(fill="x", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(
            search_card,
            placeholder_text="🔍 Rechercher un utilisateur...",
            height=36
        )

        if self.search_value:
            self.search_entry.insert(0, self.search_value)
        self.search_entry.pack(fill="x", padx=15, pady=15)

        def search_user():
            self.search_value = self.search_entry.get()
            self.refresh_widgets()

        self.search_entry.bind("<Return>", lambda event: search_user())

        # -----------------------------
        # Grid container
        # -----------------------------
        grid = ctk.CTkFrame(self, fg_color="transparent")
        grid.pack(fill="both", expand=True, padx=10, pady=5)

        columns = 3
        for i in range(columns):
            grid.grid_columnconfigure(i, weight=1, uniform="utlisateurs")

        # -----------------------------
        # User cards
        # -----------------------------
        class UserCard:
            def __init__(self, view, row, col, index, first_name, last_name, email, password, role_user, creation_date):
                card = ctk.CTkFrame(
                    grid,
                    fg_color="white",
                    corner_radius=12
                )
                card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

                # --- Top (avatar + name)
                top = ctk.CTkFrame(card, fg_color="transparent")
                top.pack(fill="x", padx=15, pady=(15, 8))

                avatar = ctk.CTkFrame(
                    top,
                    width=48,
                    height=48,
                    fg_color="#e0e7ff",
                    corner_radius=999
                )
                avatar.pack(side="left")
                avatar.pack_propagate(False)

                ctk.CTkLabel(
                    avatar,
                    text=f"{last_name[0]}{first_name[0]}",
                    font=("Arial", 16, "bold"),
                    text_color="#4f46e5"
                ).place(relx=0.5, rely=0.5, anchor="center")

                info = ctk.CTkFrame(top, fg_color="transparent")
                info.pack(side="left", padx=10)

                ctk.CTkLabel(
                    info,
                    text=f"{last_name} {first_name}",
                    font=("Arial", 13, "bold"),
                    text_color="#111827"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    info,
                    text=role_user,
                    font=("Arial", 11),
                    text_color="#6b7280"
                ).pack(anchor="w")

                # --- Infos
                body = ctk.CTkFrame(card, fg_color="transparent")
                body.pack(fill="x", padx=15, pady=5)

                ctk.CTkLabel(
                    body,
                    text=password,
                    font=("Arial", 11),
                    text_color="#374151"
                ).pack(anchor="w", pady=2)

                # --- Actions
                actions = ctk.CTkFrame(card, fg_color="transparent")
                actions.pack(fill="x", padx=15, pady=(8, 15))

                for icon, color, func in [("✏️", "#eef2ff", lambda: view.show_user_form("Modifier", index)),
                                          ("🗑️", "#fee2e2", lambda: show_delete_user_panel(index, view))]:
                    ctk.CTkButton(
                        actions,
                        text=icon,
                        width=40,
                        height=32,
                        fg_color=color,
                        text_color="#111827",
                        command=func
                    ).pack(side="left", expand=True, padx=4)

        for i, (index, first_name, last_name, email, password, role_user, creation_date) in enumerate(
                users):
            row = i // columns
            col = i % columns
            UserCard(self, row, col, index, first_name, last_name, email, password, role_user, creation_date)

    def show_user_form(self, action: str, index):

        # =============================
        # Fenêtre modale
        # =============================
        modal = ctk.CTkToplevel(self.root)
        modal.title("Nouveau utilisateur" if action == "Creer" else "Modifier utilisateur")
        modal.geometry("420x720")
        modal.resizable(False, False)
        modal.transient(self.root)

        modal.update()
        modal.grab_set()  # bloque la fenêtre principale

        modal.configure(fg_color="#f9fafb")
        modal.attributes("-alpha", 0.95)

        # Centre la fenêtre
        modal.update_idletasks()
        x = (modal.winfo_screenwidth() // 2) - (420 // 2)
        y = (modal.winfo_screenheight() // 2) - (560 // 2)
        modal.geometry(f"+{x}+{y}")

        # =============================
        # Carte blanche (contenu)
        # =============================
        card = ctk.CTkFrame(
            modal,
            fg_color="white",
            corner_radius=12
        )
        card.pack(expand=True, padx=20, pady=20, fill="both")

        # =============================
        # Header
        # =============================
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        ctk.CTkLabel(
            header,
            text="Nouveau Utilisateur" if action == "Creer" else "Modifier Utilisateur",
            font=("Arial", 18, "bold"),
            text_color="#1f2937"
        ).pack(side="left")

        ctk.CTkButton(
            header,
            text="✕",
            width=32,
            height=32,
            fg_color="transparent",
            text_color="#6b7280",
            hover_color="#e5e7eb",
            command=modal.destroy
        ).pack(side="right")

        # =============================
        # Formulaire
        # =============================
        form = ctk.CTkFrame(card, fg_color="transparent")
        form.pack(fill="both", expand=True, padx=20, pady=10)

        def field(label, placeholder, value):
            ctk.CTkLabel(
                form,
                text=label,
                font=("Arial", 12, "bold"),
                text_color="#374151"
            ).pack(anchor="w", pady=(10, 2))

            entry = ctk.CTkEntry(
                form,
                placeholder_text=placeholder,
                height=36,
                corner_radius=8
            )
            entry.pack(fill="x")

            if action == "Modifier":
                entry.insert(0, value if value else "")
            return entry

        user = self.controller.get_user(index)
        nom_entry = field("Nom *", "Nom utilisateur", user["first_name"] if user else -1)
        prenom_entry = field("Prenom *", "Prenom utilisateur", user["last_name"] if user else -1)
        email_entry = field("Email *", "email@exemple.fr", user["email"] if user else -1)
        password_entry = field("Mot de passe *", "01 23 45 67 89", user["password"].encode("utf-8") if user else -1)

        # =============================
        # User role
        # =============================company_name
        ctk.CTkLabel(
            form,
            text="Role",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        user_var = ctk.StringVar(value="commercial" if action == "Creer" else user["role_user"])
        user_select = ctk.CTkOptionMenu(
            form,
            values=["admin", "commercial"],
            variable=user_var,
            height=36,
            corner_radius=8
        )
        user_select.pack(fill="x")

        # =============================
        # Actions
        # =============================
        actions = ctk.CTkFrame(card, fg_color="transparent")
        actions.pack(fill="x", padx=20, pady=20)

        def submit():
            from datetime import datetime
            from tkinter import messagebox
            import bcrypt
            hashed_password = bcrypt.hashpw(password_entry.get().encode(), bcrypt.gensalt())
            user_data = {
                "nom": nom_entry.get(),
                "prenom": prenom_entry.get(),
                "email": email_entry.get(),
                "mot_de_passe": hashed_password.decode(),
                "role_user": user_var.get()
            }

            if user_data["nom"] == "" or user_data["prenom"] == "" or user_data["email"] == "" or \
                    user_data["mot_de_passe"] == "" or user_data["role_user"] == "":
                messagebox.showerror("ERREUR", "Tous les champs obligatoires doivent etre remplis")
            else:
                if action == "Creer":
                    self.controller.add_user(user_data)
                else:
                    self.controller.modify_user(index, user_data)
                modal.destroy()
                self.refresh_widgets()

        ctk.CTkButton(
            actions,
            text="Annuler",
            height=38,
            fg_color="white",
            border_width=1,
            border_color="#d1d5db",
            text_color="#374151",
            hover_color="#f3f4f6",
            command=modal.destroy
        ).pack(side="left", expand=True, fill="x", padx=(0, 8))

        ctk.CTkButton(
            actions,
            text=action,
            height=38,
            fg_color="#4f46e5",
            hover_color="#4338ca",
            text_color="white",
            command=submit
        ).pack(side="left", expand=True, fill="x")