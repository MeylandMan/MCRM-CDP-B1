import customtkinter as ctk

class ClientView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller

        self.pack(fill="both", expand=True)

    def create_widgets(self):
        # ----------------------------
        # Données mock (temporaire)
        # ----------------------------
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
            height=38
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

