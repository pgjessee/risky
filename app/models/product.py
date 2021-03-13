from .db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    etsy_product_id = db.Column(db.Integer, unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "etsy_product_id": self.etsy_product_id
        }

