from config import get_connection
import bcrypt

class AuthModel:

    @staticmethod
    def authenticate(email: str, password: str):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT id_user, first_name, last_name, email, password, role_user
            FROM user
            WHERE email = %s
        """
        cursor.execute(query, (email,))
        user = list(cursor.fetchone())

        conn.close()

        if user is None:
            return None

        # Vérification du mot de passe (bcrypt)
        if bcrypt.checkpw(
                password.encode("utf-8"),
                user[4].encode("utf-8")
        ):
            # On ne renvoie JAMAIS le mot de passe
            del user[4]

            return user

        return None