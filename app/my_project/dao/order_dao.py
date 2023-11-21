from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import Order

class OrderDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[Order] | None:
        return self.session.query(Order).filter_by(id=id).first()

    def create(self, order: Order) -> None:
        self.session.add(order)
        self.session.commit()

    def update(self, order: Order) -> None:
        self.session.merge(order)
        self.session.commit()

    def delete(self, id: int) -> None:
        order = self.session.query(Order).filter_by(id=id).first()
        if order:
            self.session.delete(order)
            self.session.commit()
