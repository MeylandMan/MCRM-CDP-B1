import customtkinter as ctk

class ProjectView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller

        self.pack(fill="both", expand=True)

    def create_widgets(self):
        # -----------------------------
        # Mock projets (plus tard → model)
        # -----------------------------
        projets = [
            {
                "nom": "Site Web E-commerce",
                "client": "Entreprise ABC",
                "statut": "en cours",
                "date_debut": "15/01/2024",
                "date_fin": "15/03/2024",
                "budget": "25 000 €",
                "description": "Développement d'un site e-commerce avec système de paiement"
            },
            {
                "nom": "Application Mobile",
                "client": "Tech Solutions",
                "statut": "en cours",
                "date_debut": "01/02/2024",
                "date_fin": None,
                "budget": "45 000 €",
                "description": "Application mobile iOS et Android pour la gestion de stocks"
            },
            {
                "nom": "Refonte Logo & Charte",
                "client": "Digital Agency",
                "statut": "terminé",
                "date_debut": "01/12/2023",
                "date_fin": "10/01/2024",
                "budget": "8 000 €",
                "description": "Refonte complète de l'identité visuelle"
            },
            {
                "nom": "Site Vitrine",
                "client": "Consulting Pro",
                "statut": "en attente",
                "date_debut": "01/03/2024",
                "date_fin": None,
                "budget": "5 000 €",
                "description": "Site vitrine responsive avec CMS"
            },
        ]

        # -----------------------------
        # Header
        # -----------------------------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        left = ctk.CTkFrame(header, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkLabel(
            left,
            text="Projets",
            font=("Arial", 22, "bold"),
            text_color="#111827"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text=f"{len(projets)} projets au total",
            font=("Arial", 12),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="+ Nouveau projet",
            fg_color="#4f46e5",
            height=38,
            corner_radius=8
        ).pack(side="right")

        # -----------------------------
        # Search bar
        # -----------------------------
        search_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search_frame,
            placeholder_text="Rechercher un projet...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Liste projets
        # -----------------------------
        list_frame = ctk.CTkFrame(self, fg_color="transparent")
        list_frame.pack(fill="both", expand=True, padx=5)

        for projet in projets:
            card = ctk.CTkFrame(
                list_frame,
                fg_color="white",
                corner_radius=12
            )
            card.pack(fill="x", padx=10, pady=8)

            # -----------------------------
            # Top (nom + badge)
            # -----------------------------
            top = ctk.CTkFrame(card, fg_color="transparent")
            top.pack(fill="x", padx=20, pady=(15, 5))

            left_top = ctk.CTkFrame(top, fg_color="transparent")
            left_top.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                left_top,
                text=projet["nom"],
                font=("Arial", 16, "bold"),
                text_color="#111827"
            ).pack(anchor="w")

            ctk.CTkLabel(
                left_top,
                text=f"Client : {projet['client']}",
                font=("Arial", 12),
                text_color="#6b7280"
            ).pack(anchor="w", pady=(2, 0))

            # Badge statut
            statut_colors = {
                "en cours": ("#dbeafe", "#1e40af"),
                "terminé": ("#dcfce7", "#166534"),
                "en attente": ("#fef9c3", "#854d0e")
            }

            bg, fg = statut_colors.get(projet["statut"], ("#e5e7eb", "#374151"))

            ctk.CTkLabel(
                top,
                text=projet["statut"],
                fg_color=bg,
                text_color=fg,
                corner_radius=20,
                font=("Arial", 11, "bold"),
                padx=12,
                pady=4
            ).pack(side="right")

            # -----------------------------
            # Description
            # -----------------------------
            ctk.CTkLabel(
                card,
                text=projet["description"],
                font=("Arial", 12),
                text_color="#374151",
                wraplength=900,
                justify="left"
            ).pack(padx=20, pady=8, anchor="w")

            # -----------------------------
            # dates
            # -----------------------------
            infos = ctk.CTkFrame(card, fg_color="transparent")
            infos.pack(fill="x", padx=20, pady=(5, 10))

            ctk.CTkLabel(
                infos,
                text=f"Début : {projet['date_debut']}",
                font=("Arial", 11),
                text_color="#6b7280"
            ).pack(side="left", padx=(0, 15))

            if projet["date_fin"]:
                ctk.CTkLabel(
                    infos,
                    text=f"Fin : {projet['date_fin']}",
                    font=("Arial", 11),
                    text_color="#6b7280"
                ).pack(side="left", padx=(0, 15))

            # -----------------------------
            # Actions
            # -----------------------------
            actions = ctk.CTkFrame(card, fg_color="transparent")
            actions.pack(anchor="e", padx=20, pady=(0, 15))

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