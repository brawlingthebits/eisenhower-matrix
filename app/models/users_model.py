from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String 
from app.configs.database import db

@dataclass
class UsersModel(db.Model):
    
    id: int
    name: str 
    email: str 
    password_hash: str 

    __tablename__ = "users"

    keys = {"name", "email", "password"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)