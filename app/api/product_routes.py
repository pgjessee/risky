import os
from flask import Blueprint, jsonify, session, request, make_response
import requests
from app.models import db, Review, Product, User
from datetime import datetime

API_KEY = os.environ.get('API_KEY')

products_routes = Blueprint('products', __name__)

@products_routes.route('/<int:id>', methods=['GET', 'POST'])
def utilize_individual_product(id):

    req_method = request.method

    if req_method == "GET":
        reviews = None
        product = Product.query.filter_by(etsy_product_id=id).first()

        if product:
            reviews = Review.query.filter_by(product_id=product.id).all()
            reviews = [review.to_dict() for review in reviews]
        else:
            reviews = []
        url = f"https://openapi.etsy.com/v2/listings/{id}?api_key={API_KEY}"
        # url = f"https://openapi.etsy.com/v2/listings/{id}/images?api_key={API_KEY}"
        res = requests.get(url)
        res = res.json()
        # res = res["results"][0]
        res["reviews"] = reviews
        return res

    if req_method == "POST":
        product = Product.query.filter_by(etsy_product_id=id).first()
        if not product:
            product = Product(etsy_product_id = id)
            db.session.add(product)
            db.session.commit()

        review = Review(
            user_id = 1,
            product_id = int(product.id),
            user_review = "This are a test TWOTWO lol",
            star_rating = 5,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(review)
        db.session.commit()

        return review.to_dict()






