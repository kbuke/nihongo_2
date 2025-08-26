from flask import make_response, session, request
from flask_restful import Resource
from config import db

from models.individual_interests import IndividualInterestsModel

class IndividualInterestLists(Resource):
    def get(self):
        interests = [interest.to_dict() for interest in IndividualInterestsModel.query.all()]
        return interests