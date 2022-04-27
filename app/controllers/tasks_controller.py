from http import HTTPStatus
from flask import jsonify, request
from app.configs.database import db
from app.models.categories_model import CategoriesModel
from app.models.eisenhowers_model import EisenhowersModel
from app.models.tasks_model import TasksModel
from app.package.keys_services import validate_keys

def create_task():
    expected_keys = TasksModel.keys
    task_data = request.get_json()

    try:
        validate_keys(task_data, expected_keys)

        task_data["name"] = task_data["name"].title()

        if task_data["importance"] == 1 and task_data["urgency"] == 1:
            task_data["eisenhower_id"] = 1
        if task_data["importance"] == 1 and task_data["urgency"] == 2:
            task_data["eisenhower_id"] = 2
        if task_data["importance"] == 2 and task_data["urgency"] == 1:
            task_data["eisenhower_id"] = 3
        if task_data["importance"] == 2 and task_data["urgency"] == 2:
            task_data["eisenhower_id"] = 4

        id_eisenhower = task_data["eisenhower_id"]
        eisenhower = EisenhowersModel.query.filter_by(id=id_eisenhower).first()

        categories_list = task_data.pop("categories")
        
        task = TasksModel(**task_data)

        for item in categories_list:
            
            category = CategoriesModel.query.filter_by(name=item.title()).first()
            if category:
                task.categories.append(category)
            else:
                new_category = CategoriesModel(name=item.title())
                db.session.add(new_category)
                task.categories.append(new_category)
        
        db.session.add(task)
        db.session.commit()

        return jsonify({
            "id": task.id,
            "name": task.name,
            "duration": task.duration,
            "classification": eisenhower.type,
            "categories": [category.name for category in task.categories]
        }), HTTPStatus.OK
        
    except KeyError as e:
        return e.args[0], HTTPStatus.BAD_REQUEST

def update_task(id):
    ...

def delete_task(id):
    ...
