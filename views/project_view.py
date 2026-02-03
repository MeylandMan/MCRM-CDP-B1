import customtkinter as ctk

from controllers.client_controller import ClientController
from tkinter import messagebox


def show_delete_project_panel(index, view):

    response = messagebox.askquestion("Delete confirmation", "Voulez vous VRAIMENT supprimer ce projet ?")

    if response == "yes":
        from controllers.project_controller import ProjectController
        ProjectController.delete_project(index)
        view.refresh_widgets()

class ProjectView(ctk.CTkFrame):
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
        projects = self.controller.get_projects(self.search_value)

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
            text=f"{len(projects)} projets au total",
            font=("Arial", 12),
            text_color="#6b7280"
        ).pack(anchor="w")

        ctk.CTkButton(
            header,
            text="+ Nouveau projet",
            fg_color="#4f46e5",
            height=38,
            corner_radius=8,
            command= lambda: self.show_project_form("Creer", -1)
        ).pack(side="right")

        # -----------------------------
        # Search bar
        # -----------------------------
        search_card = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        search_card.pack(fill="x", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(
            search_card,
            placeholder_text="🔍 Rechercher un projet...",
            height=36
        )
        self.search_entry.pack(fill="x", padx=15, pady=15)

        def search_project():
            self.search_value = self.search_entry.get()
            self.refresh_widgets()

        self.search_entry.bind("<Return>", lambda event: search_project())

        # -----------------------------
        # Liste projects
        # -----------------------------
        list_frame = ctk.CTkFrame(self, fg_color="transparent")
        list_frame.pack(fill="both", expand=True, padx=5)

        class ProjectCard:
            def __init__(self, view, index, name, desc, start_date, end_date, project_statut, id_client):
                self.index = index

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
                    text=name,
                    font=("Arial", 16, "bold"),
                    text_color="#111827"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    left_top,
                    text=f"Client : {ClientController.get_client(id_client)["company_name"]}",
                    font=("Arial", 12),
                    text_color="#6b7280"
                ).pack(anchor="w", pady=(2, 0))

                # Badge statut
                statut_colors = {
                    "en cours": ("#dbeafe", "#1e40af"),
                    "terminé": ("#dcfce7", "#166534"),
                    "en attente": ("#fef9c3", "#854d0e")
                }

                bg, fg = statut_colors.get(project_statut, ("#e5e7eb", "#374151"))

                ctk.CTkLabel(
                    top,
                    text=project_statut,
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
                    text=desc,
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
                    text=f"Début : {start_date}",
                    font=("Arial", 11),
                    text_color="#6b7280"
                ).pack(side="left", padx=(0, 15))

                if end_date:
                    ctk.CTkLabel(
                        infos,
                        text=f"Fin : {end_date}",
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
                    text_color="#4f46e5",
                    command=lambda: view.show_project_form("Modifier", index)
                ).pack(side="left", padx=4)

                ctk.CTkButton(
                    actions,
                    text="🗑️",
                    width=36,
                    height=32,
                    fg_color="#fee2e2",
                    text_color="#991b1b",
                    command=lambda: show_delete_project_panel(self.index, view)
                ).pack(side="left", padx=4)

        for i, (index, name, desc, start_date, end_date, project_statut, id_project) in enumerate(projects):
            ProjectCard(self, index, name, desc, start_date, end_date, project_statut, id_project)

    def show_project_form(self, action: str, index=None):

        clients = ClientController.get_clients(None)
        if len(clients) == 0:
            messagebox.showerror("ERREUR", "Veuillez enregistrer au moins un client.")
            return

        modal = ctk.CTkToplevel(self.root)
        modal.title("Nouveau projet" if action == "Creer" else "Modifier projet")
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
            text="Nouveau projet" if action == "Creer" else "Modifier projet",
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

        project = self.controller.get_project(index) if action == "Modifier" else None

        name_entry = field(
            "Nom du projet *",
            "Site vitrine / Application web",
            project["project_name"] if project else ""
        )

        # Description
        ctk.CTkLabel(
            form,
            text="Description",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        desc_entry = ctk.CTkTextbox(form, height=90, corner_radius=8)
        desc_entry.pack(fill="x")

        if project:
            desc_entry.insert("1.0", project["description"])

        start_entry = field(
            "Date de début",
            "YYYY-MM-DD",
            project["start_date"] if project else ""
        )

        end_entry = field(
            "Date de fin",
            "YYYY-MM-DD",
            project["end_date"] if project else ""
        )

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

        from controllers.project_controller import ProjectController
        current_project = ProjectController.get_project(index)
        project_client = ClientController.get_client(current_project["id_client"])["company_name"] if index != -1 else None

        client_var = ctk.StringVar(
            value=client_names[0] if action == "Creer" else project_client
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
        # Statut
        # =============================
        ctk.CTkLabel(
            form,
            text="Statut",
            font=("Arial", 12, "bold"),
            text_color="#374151"
        ).pack(anchor="w", pady=(10, 2))

        statut_var = ctk.StringVar(
            value="en cours" if action == "Creer" else project["statut"]
        )

        statut_select = ctk.CTkOptionMenu(
            form,
            values=["en cours", "terminé", "annulé"],
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
            from tkinter import messagebox

            selected_client = next(
                c for c in clients if c[1] == client_var.get()
            )

            project_data = {
                "project_name": name_entry.get(),
                "description": desc_entry.get("1.0", "end").strip(),
                "start_date": start_entry.get() or None,
                "end_date": end_entry.get() or None,
                "statut": statut_var.get(),
                "id_client": selected_client[0]
            }

            if project_data["project_name"] == "":
                messagebox.showerror("Erreur", "Le nom du projet est obligatoire")
                return

            if action == "Creer":
                self.controller.add_project(project_data)
            else:
                self.controller.modify_project(index, project_data)

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
