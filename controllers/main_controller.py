from views.main_view import MainView

class MainController:
    def __init__(self, root, user, app_controller):
        self.root = root
        self.user = user
        self.app_controller = app_controller
        self.view = MainView(root, self.user, self)
