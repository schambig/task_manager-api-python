#!/usr/bin/python3
''' Create a Flask server '''
from flask import Flask


def create_app(environment):
    ''' Create a Flask server '''
    app = Flask(__name__)

    # Use 'environment' object to set the app configuration
    app.config.from_object(environment)

    return app
