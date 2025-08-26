from models.interests import InterestModel

from flask_restful import Resource
from config import db
from flask import make_response, session, request

class InterestList(Resource):
    def post(self):
        json = request.get_json()

        try:
            new_interest = InterestModel(
                interest = json.get("interest"),
                img = json.get("img")
            )
            db.session.add(new_interest)
            db.session.commit()
            return new_interest.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}