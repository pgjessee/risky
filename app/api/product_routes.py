import os
from flask import Blueprint, jsonify, session, request, make_response
import requests

API_KEY = os.environ.get('API_KEY')

products_routes = Blueprint('products', __name__)

@products_routes.route('/<int:id>', methods=['GET'])
def get_product(id):

    req_method = request.method

    if req_method == "GET":
        url = f"https://openapi.etsy.com/v2/listings/{id}?api_key={API_KEY}"
        res = requests.get(url)
        res = res.json()
        res = res["results"][0]
        return res

    if req_method == "POST":
        pass



