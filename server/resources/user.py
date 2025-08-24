from models.user import UserModel, BusinessModel, IndividualModel

from config import db 

from flask_restful import Resource
from flask import session, make_response, request

class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in UserModel.query.all()]
        return users, 201