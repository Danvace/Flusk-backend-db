from sqlalchemy.orm import Session
from app.my_project.model.models import Review

class ReviewDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Review:
        return self.session.query(Review).filter_by(id=id).first()

    def create(self, review: Review) -> None:
        self.session.add(review)
        self.session.commit()

    def update(self, review: Review) -> None:
        self.session.merge(review)
        self.session.commit()

    def delete(self, id: int) -> None:
        review = self.session.query(Review).filter_by(id=id).first()
        if review:
            self.session.delete(review)
            self.session.commit()
