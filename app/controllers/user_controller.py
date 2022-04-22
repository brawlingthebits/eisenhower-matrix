from datetime import timedelta
from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app.configs.database import db
from app.models.users_model import UsersModel
from flask_jwt_extended import create_access_token

from app.package.keys_services import validate_keys

def user_signup():
    expected_keys = UsersModel.keys
    user_data = request.get_json()

    try:
        validate_keys(user_data, expected_keys)
        user = UsersModel(**user_data)

        db.session.add(user)
        db.session.commit()

        return jsonify(user_data), HTTPStatus.CREATED

    except KeyError as e:
        return e.args[0], HTTPStatus.BAD_REQUEST

    except IntegrityError:
       return {"error": "E-mail registered"}, HTTPStatus.CONFLICT

def user_signin():
    user_data = request.get_json()
    email = user_data["email"]
    password = user_data["password"]

    user: UsersModel = UsersModel.query.filter_by(email=email).first()

    if not user:
        return {"Message": "Email not found"}, HTTPStatus.UNAUTHORIZED

    if not user.verify_password(password):
        return {"Message": "Email and password missmatch"}, HTTPStatus.UNAUTHORIZED

    token = create_access_token(user, expires_delta=timedelta(minutes=60))
    
    return jsonify({"access_token": token}), HTTPStatus.OK