from sqlalchemy import Column, ForeignKey, Integer
from app.configs.database import db

tasks_categories = db.Table("tasks_categories",
    Column('id', Integer, primary_key=True),
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

# @dataclass
# class TasksCategories(db.Model):
#     
#     __tablename__ = "tasks_categories"
# 
#     id = Column(Integer, primary_key=True)
#     task_id = Column(Integer, ForeignKey("tasks.id"))
#     category_id = Column(Integer, ForeignKey("categories.id"))