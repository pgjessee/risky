import os
from flask import Blueprint, jsonify, session, request
import requests

API_KEY = os.environ.get('API_KEY')

products_routes = Blueprint('products', __name__)

@products_routes.route('/<int:id>', methods=['GET'])
def get_product(id):
    print(API_KEY)
    url = f"https://openapi.etsy.com/v2/listings/{id}?api_key={API_KEY}"
    res = requests.get(url)
    return res.json()


