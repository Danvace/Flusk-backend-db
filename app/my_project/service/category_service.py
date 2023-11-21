from app.my_project.dao.category_dao import CategoryDAO

class CategoryService:
    def __init__(self, db):
        self.dao = CategoryDAO(db)

    def create_category(self, category):
        return self.dao.create(category)

    def get_category(self, name):
        return self.dao.get(name)

    def update_category(self, category):
        return self.dao.update(category)

    def delete_category(self, name):
        self.dao.delete(name)
