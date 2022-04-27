from http import HTTPStatus
from flask import jsonify
from app.models.categories_model import CategoriesModel
from app.models.tasks_model import TasksModel

def all_tasks():
    categories = CategoriesModel.query.all()
    result = []

    for category in categories:
        category_data = {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "tasks": []
        }

        for task in category.tasks:
            importance = task.importance
            urgency = task.urgency

            task_data = {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "duration": task.duration,
                "classification": TasksModel.eisenhower_type(importance, urgency)
            }

            category_data["tasks"].append(task_data)

        result.append(category_data)

    return jsonify(result), HTTPStatus.OK