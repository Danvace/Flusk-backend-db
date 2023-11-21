from app.my_project.dao.order_dao import OrderDAO

class OrderService:
    def __init__(self, db):
        self.dao = OrderDAO(db)

    def create_order(self, order):
        return self.dao.create(order)

    def get_order(self, id):
        return self.dao.get(id)

    def update_order(self, order):
        return self.dao.update(order)

    def delete_order(self, id):
        self.dao.delete(id)
