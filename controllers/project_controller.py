from views.project_view import ProjectView


class ProjectController:
    def __init__(self, content):
        self.view = None

    def show_projects(self):
        self.view = ProjectView(content, self)
        self.view.create_widgets()

    def on_new_project(self):
        print("Créer un nouveau projet")

    @staticmethod
    def get_project_count(condition: str):
        from models.project_model import ProjectModel
        return ProjectModel.get_project_count(condition)