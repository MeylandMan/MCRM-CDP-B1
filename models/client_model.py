import pymysql.cursors

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

    @staticmethod
    def get_clients():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM client WHERE 1")

        clients = cursor.fetchall()

        cursor.close()
        conn.close()

        return clients

    @staticmethod
    def get_client(index):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM client WHERE id_client = %s", (index,))

        client = cursor.fetchone()

        cursor.close()
        conn.close()

        return client