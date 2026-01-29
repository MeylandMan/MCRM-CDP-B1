import customtkinter as ctk

class ContactView(ctk.CTkFrame):
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
        # Mock contacts
        # -----------------------------
        contacts = self.controller.get_contacts()

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
            corner_radius=8,
            command= lambda: self.show_contact_form("Creer", -1)
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
        class ContactCard:
            def __init__(self, view, row, col, index, first_name, last_name, email, phone, company_name, company_role, contact_notes):
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
                    text=f"{last_name[0]}{first_name[0]}",
                    font=("Arial", 16, "bold"),
                    text_color="#4f46e5"
                ).place(relx=0.5, rely=0.5, anchor="center")

                info = ctk.CTkFrame(top, fg_color="transparent")
                info.pack(side="left", padx=10)

                ctk.CTkLabel(
                    info,
                    text=f"{last_name} {first_name}",
                    font=("Arial", 13, "bold"),
                    text_color="#111827"
                ).pack(anchor="w")

                ctk.CTkLabel(
                    info,
                    text=company_role,
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

                info_line(company_name)
                info_line(email)
                info_line(phone)

                # --- Notes
                if contact_notes:
                    notes = ctk.CTkFrame(card, fg_color="#f9fafb", corner_radius=8)
                    notes.pack(fill="x", padx=15, pady=8)

                    ctk.CTkLabel(
                        notes,
                        text=contact_notes,
                        font=("Arial", 10),
                        text_color="#6b7280",
                        wraplength=260,
                        justify="left"
                    ).pack(padx=10, pady=8)

                # --- Actions
                actions = ctk.CTkFrame(card, fg_color="transparent")
                actions.pack(fill="x", padx=15, pady=(8, 15))

                for icon, color, func in [("✏️", "#eef2ff", lambda:view.show_contact_form("Modifier", index)), ("🗑️", "#fee2e2", lambda:print("Removed Contact"))]:
                    ctk.CTkButton(
                        actions,
                        text=icon,
                        width=40,
                        height=32,
                        fg_color=color,
                        text_color="#111827",
                        command=func
                    ).pack(side="left", expand=True, padx=4)

        for i, (index, first_name, last_name, email, phone, company_name, company_role, contact_notes) in enumerate(contacts):
            row = i // columns
            col = i % columns
            ContactCard(self, row, col, index, first_name, last_name, email, phone, company_name, company_role, contact_notes)

    def show_contact_form(self, action: str, index):

            # =============================
            # Fenêtre modale
            # =============================
            modal = ctk.CTkToplevel(self.root)
            modal.title("Nouveau contact" if action == "Creer" else "Modifier contact")
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
                text="Nouveau Contact" if action == "Creer" else "Modifier contact",
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

            def field(label, placeholder, value):
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

            contact = self.controller.get_contact(index)
            nom_entry = field("Nom *", "Nom du contact", contact["first_name"] if contact else -1)
            prenom_entry = field("Prenom *", "Prenom du contact", contact["last_name"] if contact else -1)
            email_entry = field("Email *", "email@exemple.fr", contact["email"] if contact else -1)
            tel_entry = field("Téléphone *", "01 23 45 67 89", contact["phone"] if contact else -1)
            company_name_entry = field("Nom de l'entreprise *", "ABC Company", contact["company_name"] if contact else -1)
            company_role = field("Role dans l'entreprise *", "PDG", contact["company_role"] if contact else -1)
            notes = field("Notes", "Decrivez le contact", contact["notes"] if contact else -1)

            # =============================
            # Actions
            # =============================
            actions = ctk.CTkFrame(card, fg_color="transparent")
            actions.pack(fill="x", padx=20, pady=20)

            def submit():
                from datetime import datetime
                from tkinter import messagebox
                contact_data = {
                    "nom": nom_entry.get(),
                    "prenom": prenom_entry.get(),
                    "email": email_entry.get(),
                    "telephone": tel_entry.get(),
                    "company_name": company_name_entry.get(),
                    "company_role": company_role.get(),
                    "notes": notes.get()
                }

                if contact_data["nom"] == "" or contact_data["prenom"] == "" or contact_data["email"] == "" or \
                        contact_data["telephone"] == "" or contact_data["company_name"] == "" or contact_data["company_role"] == "":
                    messagebox.showerror("ERREUR", "Tous les champs obligatoires doivent etre remplis")
                else:
                    if action == "Creer":
                        self.controller.add_contact(contact_data)
                    else:
                        self.controller.modify_contact(index, contact_data)
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