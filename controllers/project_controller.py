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
    def get_projects():
        return ProjectModel.get_projects()

    @staticmethod
    def get_project(index):
        return ProjectModel.get_project(index)

    @staticmethod
    def add_project(project_data):
        ProjectModel.add_project(project_data)