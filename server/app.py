from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    pass

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config) 
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return '<h3>Hello CipherNote server!</h3>'

    return app
