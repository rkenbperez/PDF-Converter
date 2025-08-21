from flask import Flask
from os import path

def create_app():
    app = Flask(__name__)
    return app