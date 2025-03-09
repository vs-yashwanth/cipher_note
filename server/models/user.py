from db import db

class UserModel(db.Model):

    __tablename__ = 'user'

    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(80), unique = True, nullable = False)
    created_on = db.Column(db.DateTime(), nullable = False)

