from views.user_view import UserView
from models.user_model import UserModel

class UserController:
    def __init__(self, content):
        self.content = content
        self.view = None

    def show_users(self):
        self.view = UserView(self.content, self)
        self.view.create_widgets()

    def on_new_user(self):
        print("Créer un nouveau user")

    @staticmethod
    def get_users_count(condition: str):
        return UserModel.get_user_count(condition)

    @staticmethod
    def get_users():
        return UserModel.get_users()

    @staticmethod
    def get_user(index):
        return UserModel.get_user(index)

    def add_user(self, user_data):
        UserModel.add_user(user_data)

    def modify_user(self, index, user_data):
        UserModel.modify_user(index, user_data)

    @staticmethod
    def delete_user(index):
        UserModel.delete_user(index)