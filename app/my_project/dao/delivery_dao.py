from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import Delivery

class DeliveryDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[Delivery] | None:
        return self.session.query(Delivery).filter_by(id=id).first()

    def create(self, delivery: Delivery) -> None:
        self.session.add(delivery)
        self.session.commit()

    def update(self, delivery: Delivery) -> None:
        self.session.merge(delivery)
        self.session.commit()

    def delete(self, id: int) -> None:
        delivery = self.session.query(Delivery).filter_by(id=id).first()
        if delivery:
            self.session.delete(delivery)
            self.session.commit()
