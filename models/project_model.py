from config import get_connection
import pymysql

class ProjectModel:

    @staticmethod
    def get_project_count(condition: str):
        conn = get_connection()
        cursor = conn.cursor()

        if condition:
            cursor.execute("SELECT COUNT(*) FROM project WHERE statut = %s", (condition,))
        else:
            cursor.execute("SELECT COUNT(*) FROM project WHERE 1")

        count = cursor.fetchone()

        conn.close()
        return count

    @staticmethod
    def get_projects():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM project WHERE 1")

        projects = cursor.fetchall()

        cursor.close()
        conn.close()

        return projects

    @staticmethod
    def get_project(index):
        conn = get_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM project WHERE id_project = %s", (index,))

        project = cursor.fetchone()

        cursor.close()
        conn.close()

        return project