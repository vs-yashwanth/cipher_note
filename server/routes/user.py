from flask import Blueprint, jsonify, request, current_app
from flask.views import MethodView
from schema import UserSchema
from models import UserModel
from marshmallow import ValidationError
from db import db

bp = Blueprint('user endpoint', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UsersView(MethodView):
    def get(self):
        users = UserModel.query.all()
        result = users_schema.dump(users)
        return jsonify(result)


class UserView(MethodView):
    def get(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            return user_schema.dump(user), 200
        return {"message": "user id not found"}, 404

    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return {"message": "user deleted successfully"}, 200
            except Exception as e:
                return e, 500
        return {"message": "user id not found"}, 404

    def post(self):
        data = request.get_json()
        try:
            data = user_schema.load(data)
            user = UserModel(**data)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user), 201

        except ValidationError as e:
            return e, 400


bp.add_url_rule('/users', view_func=UsersView.as_view(name='users'))
bp.add_url_rule('/user', view_func=UserView.as_view(name='user'))
bp.add_url_rule('/user/<int:user_id>',
                view_func=UserView.as_view(name='user_with_id'))
