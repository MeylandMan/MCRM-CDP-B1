from views.project_view import ProjectView


class ProjectController:
    def __init__(self, content):
        self.view = ProjectView(content, self)

    def show_projects(self):
        self.view.create_widgets()

    def on_new_project(self):
        print("Créer un nouveau projet")