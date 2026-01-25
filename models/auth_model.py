from config import get_connection
import pymysql
import bcrypt

class AuthModel:

    @staticmethod
    def authenticate(email: str, password: str):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        query = """
            SELECT id_user, first_name, last_name, email, password, role_user
            FROM user
            WHERE email = %s
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        conn.close()

        if user is None:
            return None

        # Vérification du mot de passe (bcrypt)
        if bcrypt.checkpw(
                password.encode("utf-8"),
                user["password"].encode("utf-8")
        ):
            # On ne renvoie JAMAIS le mot de passe
            user.pop("password")

            return user

        return None