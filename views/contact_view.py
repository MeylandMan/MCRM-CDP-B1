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

        for i, (index, first_name, last_name, email, phone, company_name, company_role, contact_notes) in enumerate(contacts):
            row = i // columns
            col = i % columns

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

            for icon, color in [("✏️", "#eef2ff"), ("🗑️", "#fee2e2")]:
                ctk.CTkButton(
                    actions,
                    text=icon,
                    width=40,
                    height=32,
                    fg_color=color,
                    text_color="#111827"
                ).pack(side="left", expand=True, padx=4)