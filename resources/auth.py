from flask import request
from database.models import User
from flask_restful import Resource
from flask_jwt_extended import create_access_token

import datetime

class SignUpApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

class LogInApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(username=body.get('username'))
        auth = user.check_password(body.get('password'))
        if(not auth):
            return {'error': 'Username or Password invalid!!!'}, 401

        expire = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expire)
        return {'token': access_token}, 200