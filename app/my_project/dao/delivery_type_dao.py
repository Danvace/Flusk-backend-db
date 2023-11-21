from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import DeliveryType

class DeliveryTypeDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, type: str) -> Type[DeliveryType] | None:
        return self.session.query(DeliveryType).filter_by(type=type).first()

    def create(self, delivery_type: DeliveryType) -> None:
        self.session.add(delivery_type)
        self.session.commit()

    def update(self, delivery_type: DeliveryType) -> None:
        self.session.merge(delivery_type)
        self.session.commit()

    def delete(self, type: str) -> None:
        delivery_type = self.session.query(DeliveryType).filter_by(type=type).first()
        if delivery_type:
            self.session.delete(delivery_type)
            self.session.commit()
