from .db import db
from .review import Review


# reviews = db.Table('reviews',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
#     db.Column('user_review', db.String(500), nullable=False),
#     db.Column('star_rating', db.Integer, nullable=False),
#     db.Column('created_at', db.DateTime, nullable=False),
#     db.Column('updated_at', db.DateTime, nullable=False))

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    etsy_product_id = db.Column(db.Integer, unique=True, nullable=False)

    # users = db.relationship('User', secondary=reviews, back_populates='products')
    reviews = db.relationship('Review', back_populates='product')

    def to_dict(self):
        return {
            "id": self.id,
            "etsy_product_id": self.etsy_product_id,
            "reviews": [review.to_dict for review in self.reviews]
        }

