from sqlalchemy.orm import Session
from app.my_project.model.models import BasketHasProduct

class BasketHasProductDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> BasketHasProduct:
        return self.session.query(BasketHasProduct).filter_by(id=id).first()

    def create(self, basket_has_product: BasketHasProduct) -> None:
        self.session.add(basket_has_product)
        self.session.commit()

    def update(self, basket_has_product: BasketHasProduct) -> None:
        self.session.merge(basket_has_product)
        self.session.commit()

    def delete(self, id: int) -> None:
        basket_has_product = self.session.query(BasketHasProduct).filter_by(id=id).first()
        if basket_has_product:
            self.session.delete(basket_has_product)
            self.session.commit()
