from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db 

@dataclass
class EisenhowersModel(db.Model):
    id: int 
    type: str 

    __tablename__ = "eisenhower"

    id = Column(Integer, primary_key=True)
    type = Column(String)