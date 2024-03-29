#!/usr/bin/python3
''' Create a Flask server '''
from flask import Flask
from .models import db
from .models.task import Task
from .views import api_v1

# Creates a new instance of a Flask web application,
# and use special variable __name__, which represents the name of the current module
app = Flask(__name__)

def create_app(environment):
    ''' Create a Flask server '''
    # Use 'environment' module that contains the configuration settings for the application.
    app.config.from_object(environment)

    # Register all routes from views module
    app.register_blueprint(api_v1)

    # Create tasks table in DB
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
