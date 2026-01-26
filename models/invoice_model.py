from config import get_connection

class InvoiceModel:

    @staticmethod
    def get_invoices_count(condition: str):
        conn = get_connection()
        cursor = conn.cursor()

        if condition:
            cursor.execute("SELECT COUNT(*) FROM invoice WHERE statut = %s", (condition,))
        else:
            cursor.execute("SELECT COUNT(*) FROM invoice WHERE 1")

        count = cursor.fetchone()

        conn.close()
        return count