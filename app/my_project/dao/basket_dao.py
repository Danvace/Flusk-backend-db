from typing import Type

from app.my_project.model.models import Basket
from sqlalchemy.orm import Session


class BasketDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[Basket] | None:
        return self.session.query(Basket).filter_by(id=id).first()

    def create(self, basket: Basket) -> None:
        self.session.add(basket)
        self.session.commit()

    def update(self, basket: Basket) -> None:
        self.session.merge(basket)
        self.session.commit()

    def delete(self, id: int) -> None:
        basket = self.session.query(Basket).filter_by(id=id).first()
        if basket:
            self.session.delete(basket)
            self.session.commit()
