from app.my_project.dao.basket_has_product_dao import BasketHasProductDAO

class BasketHasProductService:
    def __init__(self, db):
        self.dao = BasketHasProductDAO(db)

    def create_basket_has_product(self, basket_has_product):
        return self.dao.create(basket_has_product)

    def get_basket_has_product(self, id):
        return self.dao.get(id)

    def update_basket_has_product(self, id, basket_has_product):
        return self.dao.update(basket_has_product)

    def delete_basket_has_product(self, id):
        self.dao.delete(id)
