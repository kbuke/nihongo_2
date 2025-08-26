from flask import session, make_response, request
from flask_restful import Resource

from config import db 

from models.business_industry import BusinessIndustryModel

class BusinessIndustryList(Resource):
    def post(self):
        json = request.get_json()



        try:
            new_business_industry = BusinessIndustryModel(
                business_id = json.get("business_id"),
                industry_id = json.get("industry_id")
            )
            db.session.add(new_business_industry)
            db.session.commit()
            return new_business_industry.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}