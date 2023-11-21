from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import OrderHasBasket

class OrderHasBasketDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[OrderHasBasket] | None:
        return self.session.query(OrderHasBasket).filter_by(id=id).first()

    def create(self, order_has_basket: OrderHasBasket) -> None:
        self.session.add(order_has_basket)
        self.session.commit()

    def update(self, order_has_basket: OrderHasBasket) -> None:
        self.session.merge(order_has_basket)
        self.session.commit()

    def delete(self, id: int) -> None:
        order_has_basket = self.session.query(OrderHasBasket).filter_by(id=id).first()
        if order_has_basket:
            self.session.delete(order_has_basket)
            self.session.commit()
