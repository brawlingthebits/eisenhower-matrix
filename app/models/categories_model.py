from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, backref
from app.configs.database import db 
from app.models.tasks_categories_table import tasks_categories

@dataclass 
class CategoriesModel(db.Model):
    id: int 
    name: str 
    description: str 

    __tablename__ = "categories"

    keys = {"name", "description"}

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
"""     tasks = relationship(
                        "TasksModel", 
                        secondary=tasks_categories, 
                        back_populates="categories"
                        ) """