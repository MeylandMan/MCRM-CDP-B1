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

    @staticmethod
    def add_client(client_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO client (company_name, contact_name, email, phone, address, statut) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                client_data["entreprise"],
                client_data["nom"],
                client_data["email"],
                client_data["telephone"],
                client_data["address"],
                client_data["statut"],
            )
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def modify_client(index, client_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE client SET company_name=%s, contact_name=%s, email=%s, phone=%s, address=%s, statut=%s WHERE id_client = %s
        """

        cursor.execute(
            query,(
                client_data["entreprise"],
                client_data["nom"],
                client_data["email"],
                client_data["telephone"],
                client_data["address"],
                client_data["statut"],
                index,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def delete_client(index):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM client WHERE id_client=%s
        """

        cursor.execute(query, (index,))

        conn.commit()

        cursor.close()
        conn.close()

