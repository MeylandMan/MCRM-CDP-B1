from views.invoice_view import InvoiceView
from models.invoice_model import InvoiceModel

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
        return InvoiceModel.get_invoices_count(condition)

    @staticmethod
    def get_sum_month(date: str):
        return InvoiceModel.get_sum_month(date)

    @staticmethod
    def get_invoices():
        return InvoiceModel.get_invoices()
