from flask import make_response, session, request
from flask_restful import Resource
from config import db 

from models.business_interests import BusinessInterestModel

class BusinessInterestList(Resource):
    def post(self):
        json = request.get_json()

        try:
            new_business_interest = BusinessInterestModel(
                business_id = json.get("business_id"),
                interest_id = json.get("interest_id")
            )
            db.session.add(new_business_interest)
            db.session.commit()
            return new_business_interest.to_dict(), 201
        except ValueError as e:
            return{"error": [str(e)]}