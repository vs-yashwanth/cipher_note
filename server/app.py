import os
from flask import Flask

from routes import user_bp

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
        return '<h3>Hello CipherNote!</h3>'

    app.register_blueprint(user_bp)

    return app
