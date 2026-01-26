from config import get_connection

class ClientModel:

    @staticmethod
    def get_client_count(condition: str):
        conn = get_connection()
        cursor = conn.cursor()

        if condition:
            cursor.execute("SELECT COUNT(*) FROM client WHERE statut = %s", (condition,))
        else:
            cursor.execute("SELECT COUNT(*) FROM client WHERE 1")

        count = cursor.fetchone()

        conn.close()
        return count