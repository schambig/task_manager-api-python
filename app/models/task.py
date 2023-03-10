#!/usr/bin/python3
''' Task model to work with the api '''
from . import db
from sqlalchemy.event import listen # To trigger actions when a certain event happens

# Use a class (db.Model) provided by SQLAlchemy's ORM (Object-Relational Mapping) library
class Task(db.Model):
    __tablename__ = 'tasks'

    # Define the attributes for the model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())
    
    # Return title attribute when __str__() method is called
    def __str__(self):
        return self.title

# Pass a variable number of positional and keyword arguments to the function
# those arguments are collected into a tuple and dictionary respectively
def insert_tasks(*args, **kwargs):
    db.session.add(
        Task(title='Title 1', description='Description', deadline='2023-03-10 12:00:00')
    )
    db.session.add(
        Task(title='Title 2', description='Description', deadline='2023-03-10 12:00:00')
    )
    # Persist the previous tasks
    db.session.commit()

listen(Task.__table__, 'after_create', insert_tasks)