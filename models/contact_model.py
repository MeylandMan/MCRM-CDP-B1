from config import get_connection
import pymysql

class ContactModel:

    @staticmethod
    def get_contacts_count(condition: str):
        conn = get_connection()
        cursor = conn.cursor()

        if condition:
            cursor.execute("SELECT COUNT(*) FROM contact WHERE statut = %s", (condition,))
        else:
            cursor.execute("SELECT COUNT(*) FROM contact WHERE 1")

        count = cursor.fetchone()

        conn.close()
        return count

    @staticmethod
    def get_contacts():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contact WHERE 1")

        contacts = cursor.fetchall()

        cursor.close()
        conn.close()

        return contacts

    @staticmethod
    def get_contact(index):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM contact WHERE id_contact = %s", (index,))

        contact = cursor.fetchone()

        cursor.close()
        conn.close()

        return contact

    @staticmethod
    def add_contact(contact_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                INSERT INTO contact (first_name, last_name, email, phone, company_name, company_role, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s) \
                """
        cursor.execute(
            query,
            (
                contact_data["nom"],
                contact_data["prenom"],
                contact_data["email"],
                contact_data["telephone"],
                contact_data["company_name"],
                contact_data["company_role"],
                contact_data["notes"],
            )
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def modify_contact(index, contact_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                UPDATE contact \
                SET first_name=%s, 
                    last_name=%s, 
                    email=%s,
                    phone=%s,
                    company_name=%s,
                    company_role=%s,
                    notes=%s
                WHERE id_contact = %s \
                """

        cursor.execute(
            query, (
                contact_data["nom"],
                contact_data["prenom"],
                contact_data["email"],
                contact_data["telephone"],
                contact_data["company_name"],
                contact_data["company_role"],
                contact_data["notes"],
                index,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def delete_contact(index):
        conn = get_connection()
        cursor = conn.cursor()

        query = """DELETE FROM contact WHERE id_contact = %s"""

        cursor.execute(query, (index,))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def search_contacts_by_name(search_term):
        conn = get_connection()
        cursor = conn.cursor()

        filter_value = f"{search_term}%"

        query = "SELECT * FROM contact WHERE last_name LIKE %s"

        cursor.execute(query, (filter_value,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        return results