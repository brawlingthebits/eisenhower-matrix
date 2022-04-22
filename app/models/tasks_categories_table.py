from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer
from app.configs.database import db

@dataclass
class TasksCategories(db.Model):
    
    __tablename__ = "tasks_categories"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))