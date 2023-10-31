"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
import hashlib
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
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
    db.session.commit()
    return jsonify("account has been successfully created"), 200

@api.route('/login', methods=['POST'])
def access_account():

    response_body = request.get_json()
    email = response_body.get("email")
    password = response_body.get("password")
    user = User.query.filter_by(email = email).first()
    if user is None:
        return jsonify("account does not exist"), 400
    hash_password = hashlib.sha224(password.encode("utf-8")).hexdigest()
    user = User.query.filter_by(email = email, password = hash_password).first()
    if user is None:
        return jsonify("invald password"), 401
    token = create_access_token(identity = user.id)
    return jsonify(token = token), 200

@api.route('/authorize', methods=['GET'])
@jwt_required()
def verify_account():
    user_id = get_jwt_identity()
    return jsonify(user = user_id), 200