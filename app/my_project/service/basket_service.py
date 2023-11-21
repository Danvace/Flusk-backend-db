from app.my_project.dao.basket_dao import BasketDAO

class BasketService:
    def __init__(self, db):
        self.dao = BasketDAO(db)

    def create_basket(self, basket):
        return self.dao.create(basket)

    def get_basket(self, id):
        return self.dao.get(id)

    def update_basket(self, id, basket):
        return self.dao.update(basket)

    def delete_basket(self, id):
        self.dao.delete(id)
