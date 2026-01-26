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
        invoices = self.controller.get_invoices()

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
            text=f"{len(invoices)} devis au total",
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

        titles = ["Numéro", "Client", "Projet", "Montant", "Statut", "Création", "Actions"]

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
        for row_index, (index, invoice_date, amount, invoice_statut, id_client, id_project) in enumerate(invoices):
            row = ctk.CTkFrame(table, fg_color="transparent")
            row.grid(row=index, column=0, columnspan=7, sticky="ew")

            for i in range(7):
                row.grid_columnconfigure(i, weight=1)

            from datetime import datetime
            try:
                date_obj = datetime.strptime(str(invoice_date), "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("ERREUR: la date doit être au format YYYY-MM-DD HH:MM:SS")
                return None

            year = date_obj.year

            number = f"DEV-{year}-{str(index).zfill(3)}"

            (ctk.CTkLabel(row, text=number, font=("Arial", 12, "bold"), text_color="#111827")
             .grid(row=0, column=0, padx=12, pady=14, sticky="w"))

            from controllers.client_controller import ClientController
            (ctk.CTkLabel(row, text=ClientController.get_client(id_client)["contact_name"], font=("Arial", 12, "bold"), text_color="#111827")
             .grid(row=0, column=1, padx=12, pady=14, sticky="w"))

            from controllers.project_controller import ProjectController
            (ctk.CTkLabel(row, text=ProjectController.get_project(id_project)["project_name"],
                          font=("Arial", 12, "bold"),
                          text_color="#111827")
             .grid(row=0, column=2, padx=12, pady=14, sticky="w"))

            (ctk.CTkLabel(row, text=f"{amount} €".replace(",", " "), font=("Arial", 12, "bold"),
                          text_color="#111827")
             .grid(row=0, column=3, padx=12, pady=14, sticky="w"))

            bg, fg = statut_colors[invoice_statut]
            (ctk.CTkLabel(row, text=invoice_statut, font=("Arial", 12, "bold"), fg_color=bg, text_color=fg,
                          corner_radius=20)
             .grid(row=0, column=4, padx=12, pady=14, sticky="w"))

            (ctk.CTkLabel(row, text=invoice_date, font=("Arial", 12, "bold"),
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
