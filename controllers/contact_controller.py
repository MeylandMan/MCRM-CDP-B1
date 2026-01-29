from views.contact_view import ContactView
from models.contact_model import ContactModel

class ContactController:
    def __init__(self, content):
        self.view = ContactView(content, self)

    def show_contacts(self):
        self.view.create_widgets()

    def on_new_contact(self):
        print("Créer un nouveau contact")

    @staticmethod
    def get_contacts_count(condition: str):
        return ContactModel.get_contacts_count(condition)

    @staticmethod
    def get_contacts():
        return ContactModel.get_contacts()

    def get_contact(self, index):
        return ContactModel.get_contact(index)

    def add_contact(self, contact_data):
        ContactModel.add_contact(contact_data)

    def modify_contact(self, index, contact_data):
        ContactModel.modify_contact(index, contact_data)