from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import Product

class ProductDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[Product] | None:
        return self.session.query(Product).filter_by(id=id).first()

    def create(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def update(self, product: Product) -> None:
        self.session.merge(product)
        self.session.commit()

    def delete(self, id: int) -> None:
        product = self.session.query(Product).filter_by(id=id).first()
        if product:
            self.session.delete(product)
            self.session.commit()
