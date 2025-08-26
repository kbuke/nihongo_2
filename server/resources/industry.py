from flask import request, make_response, session
from flask_restful import Resource

from config import db

from models.industry import IndustryModel

class IndustryList(Resource):
    def get(self):
        industries = [industry.to_dict() for industry in IndustryModel.query.all()]
        return industries

    def post(self):
        json = request.get_json()

        try:
            new_industry = IndustryModel(
                title = json.get("title"),
                img = json.get("img")
            )
            db.session.add(new_industry)
            db.session.commit()
            return new_industry.to_dict(), 201
        except ValueError as e:
            return {"error": [str(e)]}