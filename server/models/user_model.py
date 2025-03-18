from db import db
from datetime import datetime


class UserModel(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,
                     nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False,
                           default=datetime.now())
