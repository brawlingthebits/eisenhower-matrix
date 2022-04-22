from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, backref
from app.configs.database import db 

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
    tasks = relationship(
                        "TasksModel", 
                        secondary="tasks_categories", 
                        backref=backref(name="categories")
                        )