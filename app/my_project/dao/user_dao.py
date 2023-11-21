from sqlalchemy.orm import Session
from app.my_project.model.models import User

class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> User:
        return self.session.query(User).filter_by(id=id).first()

    def create(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def update(self, user: User) -> None:
        self.session.merge(user)
        self.session.commit()

    def delete(self, id: int) -> None:
        user = self.session.query(User).filter_by(id=id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
