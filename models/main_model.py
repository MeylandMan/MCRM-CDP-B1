import pymysql.cursors

from config import get_connection

class MainModel:

    @staticmethod
    def get_first_movements():
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT movement_date, movement_text, id_user FROM movement ORDER BY id_movement DESC LIMIT 4;
        """

        cursor.execute(query)

        res = cursor.fetchall()

        conn.close()
        return res