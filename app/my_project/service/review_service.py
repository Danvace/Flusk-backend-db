from app.my_project.dao.review_dao import ReviewDAO

class ReviewService:
    def __init__(self, db):
        self.dao = ReviewDAO(db)

    def create_review(self, review):
        return self.dao.create(review)

    def get_review(self, id):
        return self.dao.get(id)

    def update_review(self, review):
        return self.dao.update(review)

    def delete_review(self, id):
        self.dao.delete(id)
