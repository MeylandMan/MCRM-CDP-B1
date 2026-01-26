import customtkinter as ctk

class ContactView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller

        self.pack(fill="both", expand=True)

    def create_widgets(self):
        # -----------------------------
        # Mock contacts
        # -----------------------------
        contacts = [
            {
                "prenom": "Jean",
                "nom": "Martin",
                "email": "jean.martin@abc.fr",
                "telephone": "06 12 34 56 78",
                "entreprise": "Entreprise ABC",
                "poste": "Directeur Commercial",
                "notes": "Contact principal pour les décisions stratégiques",
            },
            {
                "prenom": "Marie",
                "nom": "Dubois",
                "email": "marie.dubois@techsolutions.fr",
                "telephone": "06 98 76 54 32",
                "entreprise": "Tech Solutions",
                "poste": "Chef de Projet",
            },
            {
                "prenom": "Pierre",
                "nom": "Bernard",
                "email": "p.bernard@consultingpro.fr",
                "telephone": "06 11 22 33 44",
                "entreprise": "Consulting Pro",
                "poste": "CEO",
                "notes": "Très intéressé par nos services de développement web",
            },
            {
                "prenom": "Sophie",
                "nom": "Petit",
                "email": "sophie.petit@digitalagency.fr",
                "telephone": "06 55 66 77 88",
                "entreprise": "Digital Agency",
                "poste": "Responsable Marketing",
            },
            {
                "prenom": "Luc",
                "nom": "Durand",
                "email": "luc.durand@abc.fr",
                "telephone": "06 44 33 22 11",
                "entreprise": "Entreprise ABC",
                "poste": "Responsable Technique",
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
            text="Contacts",
            font=("Arial", 22, "bold"),
            text_color="#111827"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text=f"{len(contacts)} contacts au total",
            font=("Arial", 12),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="+ Nouveau contact",
            fg_color="#4f46e5",
            height=38,
            corner_radius=8
        ).pack(side="right")

        # -----------------------------
        # Search bar
        # -----------------------------
        search = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search,
            placeholder_text="Rechercher un contact...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Grid container
        # -----------------------------
        grid = ctk.CTkFrame(self, fg_color="transparent")
        grid.pack(fill="both", expand=True, padx=10, pady=5)

        columns = 3
        for i in range(columns):
            grid.grid_columnconfigure(i, weight=1, uniform="contacts")

        # -----------------------------
        # Contact cards
        # -----------------------------
        for index, c in enumerate(contacts):
            row = index // columns
            col = index % columns

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
                text=f"{c['prenom'][0]}{c['nom'][0]}",
                font=("Arial", 16, "bold"),
                text_color="#4f46e5"
            ).place(relx=0.5, rely=0.5, anchor="center")

            info = ctk.CTkFrame(top, fg_color="transparent")
            info.pack(side="left", padx=10)

            ctk.CTkLabel(
                info,
                text=f"{c['prenom']} {c['nom']}",
                font=("Arial", 13, "bold"),
                text_color="#111827"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info,
                text=c["poste"],
                font=("Arial", 11),
                text_color="#6b7280"
            ).pack(anchor="w")

            # --- Infos
            body = ctk.CTkFrame(card, fg_color="transparent")
            body.pack(fill="x", padx=15, pady=5)

            def info_line(text):
                ctk.CTkLabel(
                    body,
                    text=text,
                    font=("Arial", 11),
                    text_color="#374151"
                ).pack(anchor="w", pady=2)

            info_line(c["entreprise"])
            info_line(c["email"])
            info_line(c["telephone"])

            # --- Notes
            if "notes" in c:
                notes = ctk.CTkFrame(card, fg_color="#f9fafb", corner_radius=8)
                notes.pack(fill="x", padx=15, pady=8)

                ctk.CTkLabel(
                    notes,
                    text=c["notes"],
                    font=("Arial", 10),
                    text_color="#6b7280",
                    wraplength=260,
                    justify="left"
                ).pack(padx=10, pady=8)

            # --- Actions
            actions = ctk.CTkFrame(card, fg_color="transparent")
            actions.pack(fill="x", padx=15, pady=(8, 15))

            for icon, color in [("✏️", "#eef2ff"), ("🗑️", "#fee2e2")]:
                ctk.CTkButton(
                    actions,
                    text=icon,
                    width=40,
                    height=32,
                    fg_color=color,
                    text_color="#111827"
                ).pack(side="left", expand=True, padx=4)