import customtkinter as ctk

class ClientView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller

        self.pack(fill="both", expand=True)

    def refresh_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

    def create_widgets(self):
        clients = self.controller.get_clients()

        statut_colors = {
            "actif": ("#dcfce7", "#166534"),
            "prospect": ("#dbeafe", "#1e40af"),
            "inactif": ("#f3f4f6", "#374151"),
        }

        # ----------------------------
        # Header
        # ----------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(5, 10))

        left = ctk.CTkFrame(header, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkLabel(
            left,
            text="Clients",
            font=("Arial", 22, "bold"),
            text_color="#111827"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text=f"{len(clients)} clients au total",
            font=("Arial", 13),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="➕ Nouveau client",
            fg_color="#4f46e5",
            hover_color="#4338ca",
            corner_radius=8,
            height=38,
            command=self.show_client_form
        ).pack(side="right")

        # ----------------------------
        # Barre de recherche
        # ----------------------------
        search_card = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search_card.pack(fill="x", padx=10, pady=10)

        search_entry = ctk.CTkEntry(
            search_card,
            placeholder_text="🔍 Rechercher un client...",
            height=36
        )
        search_entry.pack(fill="x", padx=15, pady=15)

        # ----------------------------
        # Liste clients
        # ----------------------------
        list_frame = ctk.CTkFrame(self, fg_color="transparent")
        list_frame.columnconfigure(0, weight=1)
        list_frame.columnconfigure(1, weight=1)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        for i, (index, company_name, contact_name, email, phone, address, client_statut, creation_date) in enumerate(clients):
            card = ctk.CTkFrame(list_frame, fg_color="white", corner_radius=12)
            card.grid(row=i // 2, column=i % 2, padx=8, pady=8, sticky="nsew")

            # Header carte
            top = ctk.CTkFrame(card, fg_color="transparent")
            top.pack(fill="x", padx=15, pady=(15, 5))

            ctk.CTkLabel(
                top,
                text=company_name,
                font=("Arial", 15, "bold"),
                text_color="#111827"
            ).pack(anchor="w")

            ctk.CTkLabel(
                top,
                text=contact_name,
                font=("Arial", 12),
                text_color="#6b7280"
            ).pack(anchor="w")

            bg, fg = statut_colors[client_statut]
            statut = ctk.CTkLabel(
                top,
                text=client_statut,
                fg_color=bg,
                text_color=fg,
                corner_radius=20,
                font=("Arial", 11, "bold"),
                width=80,
                height=24
            )
            statut.pack(anchor="ne")

            # Infos
            infos = ctk.CTkFrame(card, fg_color="transparent")
            infos.pack(fill="x", padx=15, pady=10)

            ctk.CTkLabel(
                infos,
                text=f"📍 {address}",
                font=("Arial", 12),
                text_color="#374151"
            ).pack(anchor="w", pady=2)

            ctk.CTkLabel(
                infos,
                text=f"📧 {email}",
                font=("Arial", 12),
                text_color="#374151"
            ).pack(anchor="w", pady=2)

            ctk.CTkLabel(
                infos,
                text=f"📞 {phone}",
                font=("Arial", 12),
                text_color="#374151"
            ).pack(anchor="w", pady=2)

            # Footer
            footer = ctk.CTkFrame(card, fg_color="transparent")
            footer.pack(fill="x", padx=15, pady=(5, 15))

            ctk.CTkLabel(
                footer,
                text=f"Créé le {creation_date}",
                font=("Arial", 10),
                text_color="#9ca3af"
            ).pack(side="left")

            actions = ctk.CTkFrame(footer, fg_color="transparent")
            actions.pack(side="right")

            ctk.CTkButton(
                actions,
                text="✏️",
                width=36,
                height=32,
                fg_color="#eef2ff",
                text_color="#4f46e5"
            ).pack(side="left", padx=4)

            ctk.CTkButton(
                actions,
                text="🗑️",
                width=36,
                height=32,
                fg_color="#fee2e2",
                text_color="#991b1b"
            ).pack(side="left", padx=4)

    def show_client_form(self):

        # =============================
        # Fenêtre modale
        # =============================
        modal = ctk.CTkToplevel(self.root)
        modal.title("Nouveau client")
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
            text="Nouveau Client",
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

        def field(label, placeholder):
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
            return entry

        nom_entry = field("Nom *", "Nom du client")
        entreprise_entry = field("Entreprise *", "Nom de l'entreprise")
        email_entry = field("Email *", "email@exemple.fr")
        tel_entry = field("Téléphone *", "01 23 45 67 89")
        address_entry = field("Adresse *", "123, Rue ABC, 00000")

        # =============================
        # Statut
        # =============================
        ctk.CTkLabel(
            form,
            text="Statut",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        statut_var = ctk.StringVar(value="prospect")
        statut_select = ctk.CTkOptionMenu(
            form,
            values=["prospect", "actif", "inactif"],
            variable=statut_var,
            height=36,
            corner_radius=8
        )
        statut_select.pack(fill="x")

        # =============================
        # Actions
        # =============================
        actions = ctk.CTkFrame(card, fg_color="transparent")
        actions.pack(fill="x", padx=20, pady=20)

        def submit():
            from datetime import datetime
            from tkinter import messagebox
            client_data = {
                "nom": nom_entry.get(),
                "entreprise": entreprise_entry.get(),
                "email": email_entry.get(),
                "telephone": tel_entry.get(),
                "address": address_entry.get(),
                "statut": statut_var.get(),
                "dateCreation": datetime.now().strftime("%Y-%m-%d")
            }

            if client_data["nom"] == "" or client_data["entreprise"] == "" or client_data["email"] == "" or client_data["telephone"] == "" or client_data["address"] == "":
                messagebox.showerror("ERREUR", "Tous les champs doivent etre remplis")
            else:
                self.controller.add_client(
                    client_data["entreprise"],
                    client_data["nom"],
                    client_data["email"],
                    client_data["telephone"],
                    client_data["address"],
                    client_data["statut"]
                )
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
            text="Créer",
            height=38,
            fg_color="#4f46e5",
            hover_color="#4338ca",
            text_color="white",
            command=submit
        ).pack(side="left", expand=True, fill="x")