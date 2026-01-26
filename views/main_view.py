import customtkinter as ctk

class MainView(ctk.CTkFrame):
    def __init__(self, root, user_role, controller):
        super().__init__(root)
        self.root = root
        self.user_role = user_role
        self.controller = controller

        self.pack(expand=True, fill="both")

        # Layout principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.create_layout()

    def create_layout(self):
        self.create_sidebar()
        self.create_topbar()
        self.create_content()

        self.show_dashboard_home()

    # -------------------------------------------------
    # Sidebar
    # -------------------------------------------------
    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            fg_color="#312e81",  # indigo-900
            corner_radius=0
        )
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")
        self.sidebar.grid_propagate(False)

        # Header
        ctk.CTkLabel(
            self.sidebar,
            text="Wemby",
            font=("Arial", 22, "bold"),
            text_color="white"
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            self.sidebar,
            text=self.user_role,
            font=("Arial", 12),
            text_color="#c7d2fe"
        ).pack(pady=(0, 25))

        # Menu
        self.menu_buttons = {}

        menu_items = [
            ("dashboard", "Tableau de bord"),
            ("clients", "Clients"),
            ("projets", "Projets"),
            ("invoices", "Devis"),
            ("contacts", "Contacts"),
        ]

        for key, label in menu_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=label,
                anchor="w",
                height=42,
                corner_radius=8,
                fg_color="transparent",
                hover_color="#3730a3",
                text_color="#e0e7ff",
                command=lambda k=key: self.navigate(k)
            )
            btn.pack(fill="x", padx=15, pady=4)
            self.menu_buttons[key] = btn

        # Logout
        ctk.CTkButton(
            self.sidebar,
            text="Déconnexion",
            fg_color="transparent",
            hover_color="#3730a3",
            text_color="#e0e7ff",
            command=self.controller.logout
        ).pack(side="bottom", fill="x", padx=15, pady=20)

    # -------------------------------------------------
    # Top bar
    # -------------------------------------------------
    def create_topbar(self):
        self.topbar = ctk.CTkFrame(
            self,
            height=60,
            fg_color="white",
            corner_radius=0
        )
        self.topbar.grid(row=0, column=1, sticky="ew")
        self.topbar.grid_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="Tableau de bord",
            font=("Arial", 20, "bold"),
            text_color="#1f2937"
        )
        self.page_title.pack(side="left", padx=20)

    # -------------------------------------------------
    # Contenu principal
    # -------------------------------------------------
    def create_content(self):
        self.content = ctk.CTkFrame(
            self,
            fg_color="#f9fafb"
        )
        self.content.grid(row=1, column=1, sticky="nsew")
        self.content.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # -------------------------------------------------
    # Dashboard Home
    # -------------------------------------------------
    def show_dashboard_home(self):
        self.clear_content()
        self.page_title.configure(text="Tableau de bord")

        stats = [
            ("Clients actifs", "48", "+12%", "#3b82f6"),
            ("Projets en cours", "12", "+3", "#22c55e"),
            ("Devis envoyés", "23", "+8", "#eab308"),
            ("Contacts", "156", "+24", "#a855f7"),
        ]

        # Stats cards
        for i, (label, value, change, color) in enumerate(stats):
            card = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

            ctk.CTkLabel(
                card,
                text=change,
                text_color="#16a34a",
                font=("Arial", 12, "bold")
            ).pack(anchor="ne", padx=10, pady=5)

            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial", 26, "bold"),
                text_color="#111827"
            ).pack(pady=(10, 0))

            ctk.CTkLabel(
                card,
                text=label,
                font=("Arial", 12),
                text_color="#6b7280"
            ).pack(pady=(0, 15))

        # Chiffre d'affaires mensuel
        revenue = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        revenue.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")
        # Header
        header = ctk.CTkFrame(revenue, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(15, 5))

        ctk.CTkLabel(
            header,
            text="📈",
            font=("Arial", 18)
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text="Chiffre d'affaires mensuel",
            font=("Arial", 16, "bold"),
            text_color="#111827"
        ).pack(side="left", padx=6)

        # Zone centrale (fond dégradé simulé)
        body = ctk.CTkFrame(
            revenue,
            fg_color="#eef2ff",  # indigo-50 like
            corner_radius=12
        )
        body.pack(fill="both", expand=True, padx=15, pady=15)

        ctk.CTkLabel(
            body,
            text="€45 230",
            font=("Arial", 32, "bold"),
            text_color="#4f46e5"
        ).pack(pady=(40, 5))

        ctk.CTkLabel(
            body,
            text="Ce mois-ci",
            font=("Arial", 13),
            text_color="#4b5563"
        ).pack()

        # Activités récentes
        activities = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        activities.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            activities,
            text="Activités récentes",
            font=("Arial", 16, "bold"),
            text_color="#111827"
        ).pack(anchor="w", padx=15, pady=10)

        recent = [
            "Nouveau client : Entreprise ABC",
            "Devis #2024-003 accepté",
            "Projet Site Web terminé",
            "Nouveau contact : Marie Dubois"
        ]

        for item in recent:
            ctk.CTkLabel(
                activities,
                text="• " + item,
                font=("Arial", 12),
                text_color="#374151"
            ).pack(anchor="w", padx=20, pady=4)

        # Actions rapides
        actions = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        actions.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(
            actions,
            text="Actions rapides",
            font=("Arial", 16, "bold"),
            text_color="#111827"
        ).pack(anchor="w", padx=15, pady=10)

        buttons = [
            ("+ Nouveau client", "#4f46e5", 0),
            ("+ Nouveau projet", "#22c55e", 1),
            ("+ Nouveau devis", "#eab308", 2),
            ("+ Nouveau contact", "#a855f7", 3),
        ]

        for text, color, column in buttons:
            (ctk.CTkButton(
                actions,
                text=text,
                fg_color=color,
                height=38,
                corner_radius=8
            ).pack(side="left", padx=20, pady=6, expand=True))

    # -------------------------------------------------
    # Clients Home
    # -------------------------------------------------
    def show_clients_home(self):
        self.clear_content()
        self.page_title.configure(text="Clients")

        from controllers.client_controller import ClientController
        client_controller = ClientController(self.content)
        client_controller.show_clients()

    # -------------------------------------------------
    # Projects Home
    # -------------------------------------------------
    def show_projects_home(self):
        self.clear_content()
        self.page_title.configure(text="Projets")

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
        header = ctk.CTkFrame(self.content, fg_color="transparent")
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
        search_frame = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        search_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search_frame,
            placeholder_text="Rechercher un projet...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Liste projets
        # -----------------------------
        list_frame = ctk.CTkFrame(self.content, fg_color="transparent")
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

    # -------------------------------------------------
    # Invoices Home
    # -------------------------------------------------
    def show_invoices_home(self):
        self.clear_content()
        self.page_title.configure(text="Devis")

        # -----------------------------
        # Mock devis (plus tard → model)
        # -----------------------------
        devis = [
            {
                "id": "1",
                "numero": "DEV-2024-001",
                "client": "Entreprise ABC",
                "montant": 25000,
                "statut": "accepté",
                "date_creation": "10/01/2024",
                "date_validite": "10/02/2024",
            },
            {
                "id": "2",
                "numero": "DEV-2024-002",
                "client": "Tech Solutions",
                "montant": 45000,
                "statut": "envoyé",
                "date_creation": "25/01/2024",
                "date_validite": "25/02/2024",
            },
            {
                "id": "3",
                "numero": "DEV-2024-003",
                "client": "Consulting Pro",
                "montant": 5000,
                "statut": "brouillon",
                "date_creation": "15/02/2024",
                "date_validite": "15/03/2024",
            },
            {
                "id": "4",
                "numero": "DEV-2024-004",
                "client": "Digital Agency",
                "montant": 12000,
                "statut": "refusé",
                "date_creation": "05/01/2024",
                "date_validite": "05/02/2024",
            },
        ]

        # -----------------------------
        # Header
        # -----------------------------
        header = ctk.CTkFrame(self.content, fg_color="transparent")
        header.pack(fill="x", padx=10, pady=(10, 5))

        left = ctk.CTkFrame(header, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkLabel(
            left,
            text="Devis",
            font=("Arial", 22, "bold"),
            text_color="#111827"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left,
            text=f"{len(devis)} devis au total",
            font=("Arial", 12),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="+ Nouveau devis",
            fg_color="#4f46e5",
            height=38,
            corner_radius=8
        ).pack(side="right")

        # -----------------------------
        # Search bar
        # -----------------------------
        search_frame = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        search_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search_frame,
            placeholder_text="Rechercher un devis...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Table header
        # -----------------------------
        table = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        table.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        column_weights = [2, 2, 1.3, 1.2, 1.2, 1.2, 1.5]

        for i, w in enumerate(column_weights):
            table.grid_columnconfigure(i, weight=int(w * 10))

        header_row = ctk.CTkFrame(table, fg_color="#f9fafb")
        header_row.grid(row=0, column=0, columnspan=7, sticky="ew")

        titles = ["Numéro", "Client", "Montant", "Statut", "Création", "Validité", "Actions"]

        aligns = ["w", "w", "w", "w", "w", "w", "w"]

        for col, title in enumerate(titles):
            ctk.CTkLabel(
                header_row,
                text=title.upper(),
                font=("Arial", 11, "bold"),
                text_color="#6b7280"
            ).grid(
                row=0,
                column=col,
                padx=12,
                pady=12,
                sticky=aligns[col]
            )

            header_row.grid_columnconfigure(col, weight=table.grid_columnconfigure(col)["weight"])

        # -----------------------------
        # Statut colors
        # -----------------------------
        statut_colors = {
            "brouillon": ("#e5e7eb", "#374151"),
            "envoyé": ("#dbeafe", "#1e40af"),
            "accepté": ("#dcfce7", "#166534"),
            "refusé": ("#fee2e2", "#991b1b"),
        }

        # -----------------------------
        # Rows
        # -----------------------------
        for row_index, d in enumerate(devis, start=1):
            row = ctk.CTkFrame(table, fg_color="transparent")
            row.grid(row=row_index, column=0, columnspan=7, sticky="ew")

            for i in range(7):
                row.grid_columnconfigure(i, weight=1)
            (ctk.CTkLabel(row, text=d["numero"], font=("Arial", 12, "bold"), text_color="#111827" )
             .grid(row=0, column=0, padx=12, pady=14, sticky="w"))
            (ctk.CTkLabel(row, text=d["client"], font=("Arial", 12, "bold"), text_color="#111827")
             .grid(row=0, column=1, padx=12, pady=14, sticky="w"))
            (ctk.CTkLabel(row, text=f"{d['montant']:,} €".replace(",", " "), font=("Arial", 12, "bold"), text_color="#111827")
             .grid(row=0, column=2, padx=12, pady=14, sticky="w"))

            bg, fg = statut_colors[d["statut"]]
            (ctk.CTkLabel(row, text=d["statut"], font=("Arial", 12, "bold"), fg_color=bg, text_color=fg, corner_radius=20)
             .grid(row=0, column=3, padx=12, pady=14, sticky="w"))

            (ctk.CTkLabel(row, text=d["date_creation"], font=("Arial", 12, "bold"),
                          text_color="#111827")
             .grid(row=0, column=4, padx=12, pady=14, sticky="w"))
            (ctk.CTkLabel(row, text=d["date_validite"], font=("Arial", 12, "bold"),
                          text_color="#111827")
             .grid(row=0, column=5, padx=12, pady=14, sticky="w"))

            actions = ctk.CTkFrame(row, fg_color="transparent")
            actions.grid(row=0, column=6, padx=12, pady=14, sticky="w")

            for icon in ["👁️", "⬇️", "✏️", "🗑️"]:
                ctk.CTkButton(
                    actions,
                    text=icon,
                    width=32,
                    height=30,
                    fg_color="#f3f4f6",
                    text_color="#374151"
                ).pack(side="left", padx=2)

            row.grid_rowconfigure(0, minsize=56)

    # -------------------------------------------------
    # Contacts Home
    # -------------------------------------------------
    def show_contacts_home(self):
        self.clear_content()
        self.page_title.configure(text="Contacts")

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
        header = ctk.CTkFrame(self.content, fg_color="transparent")
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
        search = ctk.CTkFrame(self.content, fg_color="white", corner_radius=12)
        search.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search,
            placeholder_text="Rechercher un contact...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Grid container
        # -----------------------------
        grid = ctk.CTkFrame(self.content, fg_color="transparent")
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

    # -------------------------------------------------
    # Navigation
    # -------------------------------------------------
    def navigate(self, page):
        for btn in self.menu_buttons.values():
            btn.configure(fg_color="transparent")

        self.menu_buttons[page].configure(fg_color="#4338ca")

        match page:
            case "dashboard":
                self.show_dashboard_home()
            case "clients":
                self.show_clients_home()
            case "projets":
                self.show_projects_home()
            case "invoices":
                self.show_invoices_home()
            case "contacts":
                self.show_contacts_home()
            case _:
                self.clear_content()
                self.page_title.configure(text=page.capitalize())
