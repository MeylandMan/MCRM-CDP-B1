import customtkinter as ctk

from controllers.invoice_controller import InvoiceController

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
            ("projects", "Projets"),
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

        from controllers.client_controller import ClientController
        active_clients = ClientController(self.content).get_clients_count("actif")

        from controllers.project_controller import ProjectController
        active_projects = ProjectController(self.content).get_project_count("en cours")


        sent_invoices = InvoiceController(self.content).get_invoices_count("envoyé")

        from controllers.contact_controller import ContactController
        contacts = ContactController.get_contacts_count("")

        stats = [
            ("Clients actifs", active_clients, "+12%", "#3b82f6"),
            ("Projets en cours", active_projects, "+3", "#22c55e"),
            ("Devis envoyés", sent_invoices, "+8", "#eab308"),
            ("Contacts", contacts, "+24", "#a855f7"),
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

        from datetime import datetime
        date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sum = InvoiceController.get_sum_month(date)

        ctk.CTkLabel(
            body,
            text=f"€{sum}",
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
            ("+ Nouveau client", "#4f46e5", "clients"),
            ("+ Nouveau projet", "#22c55e", "projects"),
            ("+ Nouveau devis", "#eab308", "invoices"),
            ("+ Nouveau contact", "#a855f7", "contacts"),
        ]



        for text, color, key in buttons:
            (ctk.CTkButton(
                actions,
                text=text,
                fg_color=color,
                height=38,
                corner_radius=8,
                command=lambda k=key: self.navigate(k)
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

        from controllers.project_controller import ProjectController
        project_controller = ProjectController(self.content)
        project_controller.show_projects()

    # -------------------------------------------------
    # Invoices Home
    # -------------------------------------------------
    def show_invoices_home(self):
        self.clear_content()
        self.page_title.configure(text="Devis")

        from controllers.invoice_controller import InvoiceController
        invoice_controller = InvoiceController(self.content)
        invoice_controller.show_invoices()

    # -------------------------------------------------
    # Contacts Home
    # -------------------------------------------------
    def show_contacts_home(self):
        self.clear_content()
        self.page_title.configure(text="Contacts")

        from controllers.contact_controller import ContactController
        contact_controller = ContactController(self.content)
        contact_controller.show_contacts()

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
            case "projects":
                self.show_projects_home()
            case "invoices":
                self.show_invoices_home()
            case "contacts":
                self.show_contacts_home()
            case _:
                self.clear_content()
                self.page_title.configure(text=page.capitalize())
