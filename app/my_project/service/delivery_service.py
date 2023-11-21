from app.my_project.dao.delivery_dao import DeliveryDAO

class DeliveryService:
    def __init__(self, db):
        self.dao = DeliveryDAO(db)

    def create_delivery(self, delivery):
        return self.dao.create(delivery)

    def get_delivery(self, id):
        return self.dao.get(id)

    def update_delivery(self, delivery):
        return self.dao.update(delivery)

    def delete_delivery(self, id):
        self.dao.delete(id)
