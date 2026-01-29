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

    @staticmethod
    def add_project(project_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO project (project_name, description, start_date, end_date, statut, id_client) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                project_data["project_name"],
                project_data["description"],
                project_data["start_date"],
                project_data["end_date"],
                project_data["statut"],
                project_data["id_client"],
            )
        )
        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def modify_project(index, project_data):
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                UPDATE project \
                SET project_name=%s, \
                    description=%s, \
                    start_date=%s, \
                    end_date=%s, \
                    statut=%s, \
                    id_client=%s
                WHERE id_project = %s
                """

        cursor.execute(
            query, (
                project_data["project_name"],
                project_data["description"],
                project_data["start_date"],
                project_data["end_date"],
                project_data["statut"],
                project_data["id_client"],
                index,
            )
        )

        conn.commit()

        cursor.close()
        conn.close()