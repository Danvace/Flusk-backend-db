from sqlalchemy.orm import Session
from app.my_project.model.models import Image

class ImageDAO:
    def __init__(self, session: Session):
        self.session = session

    def get(self, id: int) -> Image:
        return self.session.query(Image).filter_by(id=id).first()

    def create(self, image: Image) -> None:
        self.session.add(image)
        self.session.commit()

    def update(self, image: Image) -> None:
        self.session.merge(image)
        self.session.commit()

    def delete(self, id: int) -> None:
        image = self.session.query(Image).filter_by(id=id).first()
        if image:
            self.session.delete(image)
            self.session.commit()
