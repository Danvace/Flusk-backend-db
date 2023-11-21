from typing import Type

from sqlalchemy.orm import Session
from app.my_project.model.models import Characteristic

class CharacteristicDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Type[Characteristic] | None:
        return self.session.query(Characteristic).filter_by(id=id).first()

    def create(self, characteristic: Characteristic) -> None:
        self.session.add(characteristic)
        self.session.commit()

    def update(self, characteristic: Characteristic) -> None:
        self.session.merge(characteristic)
        self.session.commit()

    def delete(self, id: int) -> None:
        characteristic = self.session.query(Characteristic).filter_by(id=id).first()
        if characteristic:
            self.session.delete(characteristic)
            self.session.commit()
