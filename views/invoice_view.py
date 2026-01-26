import customtkinter as ctk

class InvoiceView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color="transparent")
        self.root = root
        self.controller = controller

        self.pack(fill="both", expand=True)
    def create_widgets(self):
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
        header = ctk.CTkFrame(self, fg_color="transparent")
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
        search_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkEntry(
            search_frame,
            placeholder_text="Rechercher un devis...",
            height=38
        ).pack(fill="x", padx=15, pady=12)

        # -----------------------------
        # Table header
        # -----------------------------
        table = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
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