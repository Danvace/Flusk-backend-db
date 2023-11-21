from typing import Type

from app.my_project.model.models import Category
from sqlalchemy.orm import Session


class CategoryDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, name: str) -> Type[Category] | None:
        return self.session.query(Category).filter_by(name=name).first()

    def create(self, category: Category) -> None:
        self.session.add(category)
        self.session.commit()

    def delete(self, name: str) -> None:
        category = self.session.query(Category).filter_by(name=name).first()
        if category is not None:
            self.session.delete(category)
            self.session.commit()

    def update(self, category: Category) -> None:
        self.session.merge(category)
        self.session.commit()
