#!/usr/bin/python3
''' Create a Flask server '''
from flask import Flask

app = Flask(__name__)


def create_app():
    ''' Create a Flask server '''
    return app
