from app.my_project.dao.order_has_basket_dao import OrderHasBasketDAO

class OrderHasBasketService:
    def __init__(self, db):
        self.dao = OrderHasBasketDAO(db)

    def create_order_has_basket(self, order_has_basket):
        return self.dao.create(order_has_basket)

    def get_order_has_basket(self, id):
        return self.dao.get(id)

    def update_order_has_basket(self, order_has_basket):
        return self.dao.update(order_has_basket)

    def delete_order_has_basket(self, id):
        self.dao.delete(id)
