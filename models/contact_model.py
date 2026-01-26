from config import get_connection

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