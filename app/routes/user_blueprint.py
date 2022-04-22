from flask import Blueprint
from app.controllers.user_controller import user_signup, user_signin

bp_users = Blueprint("bp_users", __name__)

bp_users.post("/signup")(user_signup)
bp_users.post("/signin")(user_signin)