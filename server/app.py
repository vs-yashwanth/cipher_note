import os
from flask import Flask

from models import UserModel

from db import db

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config) 
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello_world():
        return '<h3>Hello CipherNote server!</h3>'

    return app
