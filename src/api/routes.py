"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
import hashlib
api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def create_account():

    response_body = request.get_json()
    email = response_body.get("email")
    password = response_body.get("password")
    user = User.query.filter_by(email = email).first()
    if user is not None:
        return jsonify("account already exist"), 403
    hash_password = hashlib.sha224(password.encode("utf-8")).hexdigest()
    new_user = User(email = email, password = hash_password)
    db.session.add(new_user)
    db.sessiom.commit()
    return jsonify("account has been successfully created"), 200