from .db import db

order_products = db.Table('order_products',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), nullable=False),
    db.Column('purchase_quantity', db.Integer, nullable=False))

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    products = db.relationship('Product', secondary=order_products, back_populates='orders')
    user = db.relationship('User', back_populates='orders')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "subtotal": self.subtotal,
            "total": self.total
        }



