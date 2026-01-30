from views.project_view import ProjectView
from models.project_model import ProjectModel

class ProjectController:
    def __init__(self, content):
        self.view = None
        self.content = content

    def show_projects(self):
        self.view = ProjectView(self.content, self)
        self.view.create_widgets()

    def on_new_project(self):
        print("Créer un nouveau projet")

    @staticmethod
    def get_project_count(condition: str):
        return ProjectModel.get_project_count(condition)

    @staticmethod
    def get_projects(search_term):
        if not search_term:
            return ProjectModel.get_projects()
        else:
            return ProjectModel.search_projects_by_name(search_term)

    @staticmethod
    def get_project(index):
        return ProjectModel.get_project(index)

    @staticmethod
    def add_project(project_data):
        ProjectModel.add_project(project_data)

    def modify_project(self, index, project_data):
        ProjectModel.modify_project(index, project_data)

    @staticmethod
    def delete_project(index):
        ProjectModel.delete_project(index)