#!/usr/bin/python3
''' Task model to work with the api '''
from . import db

# Use a class (db.Model) provided by SQLAlchemy's ORM (Object-Relational Mapping) library
class Task(db.Model):
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