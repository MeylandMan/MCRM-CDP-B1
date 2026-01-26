from config import get_connection

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