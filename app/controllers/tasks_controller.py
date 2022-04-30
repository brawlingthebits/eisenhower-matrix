from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.exc import DataError, IntegrityError, NoResultFound
from app.configs.database import db
from app.exceptions.keys_exceptions import MissingKeys
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
    
    except MissingKeys as e:
        e.args[0], HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "Task already exists"}, HTTPStatus.CONFLICT

def update_task(task_id: int):
    task_data = request.get_json()

    try:
        data_to_update = TasksModel.query.filter_by(id=task_id).one_or_none()

        if data_to_update == None:
            return {"error": "Category not found"}, HTTPStatus.BAD_REQUEST
        

        for key, value in task_data.items():
            setattr(data_to_update, key, value) 
        
        type_eisenhower = TasksModel.eisenhower_type(task_data.importance, task_data.urgency)
        eisenhower = EisenhowersModel.query.filter_by(type=type_eisenhower).first()
        task_data["eisenhower_id"] = eisenhower.id
        
        db.session.add(data_to_update)
        db.session.commit()
        
        return jsonify({
            "id": task_data.id,
            "name": task_data.name,
            "duration": task_data.duration,
            "classification": eisenhower.type,
            "categories": [category.name for category in task_data.categories]
        }), HTTPStatus.OK


    except DataError:
        return {"error": "Id must be an integer"}, HTTPStatus.BAD_REQUEST
        
    except IntegrityError:
        return {"error": "Task already exists"}, HTTPStatus.CONFLICT

def delete_task(task_id: int):
    try: 
        data_to_delete = TasksModel.query.filter_by(id=task_id).first()
        
        db.session.delete(data_to_delete)
        db.session.commit()

        return "", HTTPStatus.OK

    except NoResultFound:
        return {"error": "Id not found"}, HTTPStatus.BAD_REQUEST
