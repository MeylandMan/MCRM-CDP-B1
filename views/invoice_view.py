import customtkinter as ctk
from tkinter import messagebox




def show_delete_project_panel(index, view):

    response = messagebox.askquestion("Delete confirmation", "Voulez vous VRAIMENT supprimer ce devis ?")

    if response == "yes":
        from controllers.invoice_controller import InvoiceController
        InvoiceController.delete_invoice(index)
        view.refresh_widgets()


class InvoiceView(ctk.CTkFrame):
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
        # -----------------------------
        # Mock devis
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
            corner_radius=8,
            command=lambda: self.show_invoice_form("Creer", -1)
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
        class InvoiceCard:
            def __init__(self, index, invoice_date, amount, invoice_statut, id_client, id_project):
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
                (ctk.CTkLabel(row, text=ClientController.get_client(id_client)["contact_name"],
                              font=("Arial", 12, "bold"), text_color="#111827")
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
        for row_index, (index, invoice_date, amount, invoice_statut, id_client, id_project) in enumerate(invoices):
            InvoiceCard(index, invoice_date, amount, invoice_statut, id_client, id_project)

    def show_invoice_form(self, action: str, index=None):
        from controllers.project_controller import ProjectController
        from controllers.client_controller import ClientController
        clients = ClientController.get_clients(None)
        projects = ProjectController.get_projects(None)

        if len(clients) == 0 or len(projects) == 0:
            messagebox.showerror("ERREUR", "Veuillez enregistrer au moins un client et projet.")
            return

        modal = ctk.CTkToplevel(self.root)
        modal.title("Nouveau devis" if action == "Creer" else "Modifier devis")
        modal.geometry("460x760")
        modal.resizable(False, False)
        modal.transient(self.root)

        modal.update()
        modal.grab_set()

        modal.configure(fg_color="#f9fafb")
        modal.attributes("-alpha", 0.95)

        modal.update_idletasks()
        x = (modal.winfo_screenwidth() // 2) - (460 // 2)
        y = (modal.winfo_screenheight() // 2) - (760 // 2)
        modal.geometry(f"+{x}+{y}")

        # =============================
        # Card
        # =============================
        card = ctk.CTkFrame(modal, fg_color="white", corner_radius=12)
        card.pack(expand=True, padx=20, pady=20, fill="both")

        # =============================
        # Header
        # =============================
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        ctk.CTkLabel(
            header,
            text="Nouveau devis" if action == "Creer" else "Modifier devis",
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
        # Form
        # =============================
        form = ctk.CTkFrame(card, fg_color="transparent")
        form.pack(fill="both", expand=True, padx=20, pady=10)

        def field(label, placeholder, value=""):
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

        invoice = self.controller.get_invoice(index) if action == "Modifier" else None

        name_entry = field(
            "Montant *",
            "12345",
            invoice["amount"] if invoice else ""
        )

        # =============================
        # Statut
        # =============================
        ctk.CTkLabel(
            form,
            text="Statut",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        statut_var = ctk.StringVar(value="brouillon" if action == "Creer" else invoice["statut"])
        statut_select = ctk.CTkOptionMenu(
            form,
            values=["brouillon", "envoyé", "accepté", "refusé"],
            variable=statut_var,
            height=36,
            corner_radius=8
        )
        statut_select.pack(fill="x")

        # =============================
        # Client select
        # =============================
        ctk.CTkLabel(
            form,
            text="Client *",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))


        client_names = [c[1] for c in clients]

        from controllers.invoice_controller import InvoiceController
        current_invoice = InvoiceController.get_invoice(index)
        invoice_client = ClientController.get_client(current_invoice["id_client"])["company_name"] if index != -1 else None

        client_var = ctk.StringVar(
            value=client_names[0] if action == "Creer" else invoice_client
        )

        client_select = ctk.CTkOptionMenu(
            form,
            values=client_names,
            variable=client_var,
            height=36,
            corner_radius=8
        )
        client_select.pack(fill="x")

        # =============================
        # Project select
        # =============================
        ctk.CTkLabel(
            form,
            text="Projet *",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        project_names = [p[1] for p in projects]

        invoice_project = ProjectController.get_project(current_invoice["id_project"])["project_name"] if index != -1 else None

        project_var = ctk.StringVar(
            value=project_names[0] if action == "Creer" else invoice_project
        )

        project_select = ctk.CTkOptionMenu(
            form,
            values=project_names,
            variable=project_var,
            height=36,
            corner_radius=8
        )
        project_select.pack(fill="x")

        # =============================
        # Actions
        # =============================
        actions = ctk.CTkFrame(card, fg_color="transparent")
        actions.pack(fill="x", padx=20, pady=20)

        def submit():
            selected_client = next(
                c for c in clients if c[1] == client_var.get()
            )
            selected_project = next(
                p for p in projects if p[1] == project_var.get()
            )

            invoice_data = {
                "amount": name_entry.get(),
                "statut": statut_var.get(),
                "id_client": selected_client[0],
                "id_project": selected_project[0]
            }

            if invoice_data["amount"] == "":
                messagebox.showerror("Erreur", "Le montant est obligatoire")
                return
            if not invoice_data["amount"].is_digit():
                messagebox.showerror("Erreur", "Entrez un montant correct")
                return

            if action == "Creer":
                self.controller.add_invoice(invoice_data)
            else:
                self.controller.modify_invoice(index, invoice_data)

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