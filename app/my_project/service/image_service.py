from app.my_project.dao.image_dao import ImageDAO

class ImageService:
    def __init__(self, db):
        self.dao = ImageDAO(db)

    def create_image(self, image):
        return self.dao.create(image)

    def get_image(self, id):
        return self.dao.get(id)

    def update_image(self, image):
        return self.dao.update(image)

    def delete_image(self, id):
        self.dao.delete(id)
