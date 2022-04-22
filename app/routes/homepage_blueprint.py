from flask import Blueprint
from app.controllers.homepage_controller import all_tasks

bp_homepage = Blueprint("bp_homepage", __name__)

bp_homepage.get("/")(all_tasks)