from app.my_project.dao.delivery_type_dao import DeliveryTypeDAO

class DeliveryTypeService:
    def __init__(self, db):
        self.dao = DeliveryTypeDAO(db)

    def create_delivery_type(self, delivery_type):
        return self.dao.create(delivery_type)

    def get_delivery_type(self, type):
        return self.dao.get(type)

    def update_delivery_type(self, delivery_type):
        return self.dao.update(delivery_type)

    def delete_delivery_type(self, type):
        self.dao.delete(type)
