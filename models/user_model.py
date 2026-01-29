import pymysql.cursors

from config import get_connection

class UserModel:

    @staticmethod
    def get_user_count(condition: str):
        conn = get_connection()
        cursor = conn.cursor()

        if condition:
            cursor.execute("SELECT COUNT(*) FROM user WHERE statut = %s", (condition,))
        else:
            cursor.execute("SELECT COUNT(*) FROM user WHERE 1")

        count = cursor.fetchone()

        conn.close()
        return count

    @staticmethod
    def get_users():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE 1")

        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return users

    @staticmethod
    def get_user(index):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM user WHERE id_user = %s", (index,))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user

    @staticmethod
    def add_user(user_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO user (first_name, last_name, email, password, role_user) VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                user_data["nom"],
                user_data["prenom"],
                user_data["email"],
                user_data["mot_de_passe"],
                user_data["role_user"],
            )
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def modify_user(index, user_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE user SET first_name=%s, last_name=%s, email=%s, password=%s, role_user=%s WHERE id_user = %s
        """

        cursor.execute(
            query,(
                user_data["nom"],
                user_data["prenom"],
                user_data["email"],
                user_data["mot_de_passe"],
                user_data["role_user"],
                index,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def delete_user(index):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM user WHERE id_user=%s
        """

        cursor.execute(query, (index,))

        conn.commit()

        cursor.close()
        conn.close()

