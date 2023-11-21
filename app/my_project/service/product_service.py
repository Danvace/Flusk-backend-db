from app.my_project.dao.product_dao import ProductDAO

class ProductService:
    def __init__(self, db):
        self.dao = ProductDAO(db)

    def create_product(self, product):
        return self.dao.create(product)

    def get_product(self, id):
        return self.dao.get(id)

    def update_product(self, product):
        return self.dao.update(product)

    def delete_product(self, id):
        self.dao.delete(id)
