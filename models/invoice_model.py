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

        cursor.close()
        conn.close()
        return count

    @staticmethod
    def get_sum_month(date: str):
        from datetime import datetime

        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("ERREUR: la date doit être au format YYYY-MM-DD HH:MM:SS")
            return None

        year = date_obj.year
        month = date_obj.month

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT COALESCE(SUM(amount), 0) FROM invoice 
            WHERE statut = 'accepté' 
            AND YEAR(invoice_date) = %s 
            AND MONTH(invoice_date) = %s
        """

        cursor.execute(query, (year, month,))

        count = cursor.fetchone()

        cursor.close()
        conn.close()

        return count[0]

