from app.my_project.dao.characteristic_dao import CharacteristicDAO

class CharacteristicService:
    def __init__(self, db):
        self.dao = CharacteristicDAO(db)

    def create_characteristic(self, characteristic):
        return self.dao.create(characteristic)

    def get_characteristic(self, id):
        return self.dao.get(id)

    def update_characteristic(self, characteristic):
        return self.dao.update(characteristic)

    def delete_characteristic(self, id):
        self.dao.delete(id)
