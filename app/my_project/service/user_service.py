from app.my_project.dao.user_dao import UserDAO

class UserService:
    def __init__(self, db):
        self.dao = UserDAO(db)

    def create_user(self, user):
        return self.dao.create(user)

    def get_user(self, id):
        return self.dao.get(id)

    def update_user(self, user):
        return self.dao.update(user)

    def delete_user(self, id):
        self.dao.delete(id)
