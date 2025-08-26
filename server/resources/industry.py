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

class Industry(Resource):
    def get(self, id):
        industry = IndustryModel.query.filter(IndustryModel.id==id).first()
        if industry:
            return make_response(industry.to_dict())
        else:
            return {"message": f"Industry {id} not found"}, 404
    
    def patch(self, id):
        data = request.get_json()

        industry = IndustryModel.query.filter(IndustryModel.id==id).first()

        if industry:
            try:
                for attr in data:
                    setattr(industry, attr, data[attr])
                db.session.add(industry)
                db.session.commit()
                return make_response(industry.to_dict())
            except ValueError as e:
                return {"message": [str(e)]}
        else:
            return{"message": f"Industry {id} not found"}, 404
        
    def delete(self, id):
        industry = IndustryModel.query.filter(IndustryModel.id==id).first()
        if industry:
            db.session.delete(industry)
            db.session.commit()
            return{"message": f"Industry {id} deleted."}
        else:
            return{"message": f"Industry {id} not found."}, 404