from views.invoice_view import InvoiceView


class InvoiceController:
    def __init__(self, content):
        self.view = None
        self.content = content

    def show_invoices(self):
        self.view = InvoiceView(self.content, self)
        self.view.create_widgets()

    def on_new_invoice(self):
        print("Créer un nouveau devis")

    @staticmethod
    def get_invoices_count(condition: str):
        from models.invoice_model import InvoiceModel
        return InvoiceModel.get_invoices_count(condition)