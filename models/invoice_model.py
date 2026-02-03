from config import get_connection
import pymysql

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

    @staticmethod
    def get_invoices():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM invoice WHERE 1")

        invoices = cursor.fetchall()

        cursor.close()
        conn.close()

        return invoices
    

    @staticmethod
    def get_invoice(index):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM invoice WHERE id_invoice = %s", (index,))

        invoice = cursor.fetchone()

        cursor.close()
        conn.close()

        return invoice

    @staticmethod
    def add_invoice(invoice_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO invoice (amount, statut, id_client, id_project) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                invoice_data["amount"],
                invoice_data["statut"],
                invoice_data["id_client"],
                invoice_data["id_project"],
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def modify_invoice(index, invoice_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE invoice SET amount=%s, statut=%s, id_client=%s, id_project=%s WHERE id_invoice = %s
        """

        cursor.execute(
            query,(
                invoice_data["amount"],
                invoice_data["statut"],
                invoice_data["id_client"],
                invoice_data["id_project"],
                index,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def delete_invoice(index):
        conn = get_connection()
        cursor = conn.cursor()

        query = """DELETE FROM invoice WHERE id_invoice = %s"""
        cursor.execute(query, (index,))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def search_invoices_by_name(search_term):
        # TBA
        pass

