from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from app.configs.database import db 

@dataclass
class EisenhowersModel(db.Model):
    id: int 
    type: str 

    __tablename__ = "eisenhower"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    tasks = relationship("TasksModel", backref=backref("eisenhower", uselist=False))