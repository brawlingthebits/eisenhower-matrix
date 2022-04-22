from dataclasses import dataclass
from marshmallow import validates
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from app.configs.database import db

@dataclass
class TasksModel(db.Model):
    id: int 
    name: str 
    description: str 
    duration: int 
    importance: int 
    urgency: int 

    __tablename__ = "tasks"

    keys = {"name", "description", "duration", "importance", "urgency", "categories"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer, nullable=False)
    urgency = Column(Integer, nullable=False)
    eisenhower_id = Column(
                            Integer, 
                            ForeignKey("eisenhower.id")
                        )

    @classmethod
    def eisenhower_type(cls, importance, urgency):
        eisenhower_types = {
            (1,1): "Do it first",
            (1,2): "Delegate it",
            (2,1): "Schedule it",
            (2,2): "Delete it"
        }

        return eisenhower_types[importance, urgency]
