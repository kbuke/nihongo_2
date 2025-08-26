from models.user import UserModel, BusinessModel, IndividualModel

from models.city import CityModel

from config import db 

from flask_restful import Resource
from flask import session, make_response, request

import re

class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in UserModel.query.all()]
        return users, 201
    
    def post(self):
        json=request.get_json()

        account_type = json.get("ac_type")

        # handle logic for registered email
        new_email = json.get("email")
        pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if pattern.match(new_email):
            new_email=new_email
        else:
            return{"message": "email address is not valid."}, 422

        if account_type=="business":
            city_id = json.get("city_id")
            city = CityModel.query.filter(CityModel.id==city_id).first()

            if city:
                new_business = BusinessModel(
                    email=new_email,
                    ac_type=account_type,
                    name=json.get("name"),
                    postal_code=json.get("postal_code"),
                    district_block=json.get("district_block"),
                    building_name=json.get("building_name"),
                    floor_room=json.get("floor_room"),
                    allow_email=json.get("allow_email"),
                    city_id=city_id
                )
                db.session.add(new_business)
                db.session.commit()
                return new_business.to_dict(), 201
            
            else:
                return{"error": f"No city with id: {city_id}"}
        
        elif account_type=="individual":
            new_business = IndividualModel(
                email=json.get("email"),
                ac_type=account_type,
                first_name=json.get("first_name"),
                last_name=json.get("last_name"),
                intro=json.get("intro")
            )
            db.session.add(new_business)
            db.session.commit()
            return new_business.to_dict(), 201
        else:
            return {"message": "Please enter a proper account type"}, 401
        
class User(Resource):
    def get(self, id):
        user = UserModel.query.filter(UserModel.id==id).first()
        # breakpoint()
        if user:
            return user.to_dict(), 201
        else:
            return {"message": "User not found"}, 404
    
    def patch(self, id):
        data = request.get_json()

        user = UserModel.query.filter(UserModel.id==id).first()

        if user:
            try:
                for attr in data:
                    setattr(user, attr, data[attr])
                db.session.add(user)
                db.session.commit()
                return make_response(user.to_dict(), 202)
            except ValueError as e:
                return {"message": [str(e)]}, 400
        return{"message": "User not found"}, 404

class IndividualList(Resource):
    def get(self):
        individuals = [individual.to_dict() for individual in IndividualModel.query.all()]
        return individuals

class Individual(Resource):
    def get(self, id):
        individual = IndividualModel.query.filter(IndividualModel.id==id).first()
        if individual:
            return individual.to_dict(), 201
        else:
            return {"message": "Individual not found"}, 404

class BusinessList(Resource):
    def get(self):
        businesses = [business.to_dict() for business in BusinessModel.query.all()]
        return businesses
    
class Business(Resource):
    def get(self, id):
        business = BusinessModel.query.filter(BusinessModel.id==id).first()
        if business:
            return business.to_dict(), 201
        else:
            return {"message": "Business not found."}, 404
