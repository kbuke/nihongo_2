from flask import make_response, session, request
from flask_restful import Resource
from config import db

from models.individual_interests import IndividualInterestsModel

class IndividualInterestLists(Resource):
    def get(self):
        interests = [interest.to_dict() for interest in IndividualInterestsModel.query.all()]
        return interests
    
    def post(self):
        json = request.get_json()

        try:
            new_interest = IndividualInterestsModel(
                individual_id=json.get("individual_id"),
                interests_id=json.get("interests_id")
            )
            db.session.add(new_interest)
            db.session.commit()
            return new_interest.to_dict(), 201
        
        except ValueError as e:
            return {"message": [str(e)]}