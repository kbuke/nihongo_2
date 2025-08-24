from models.user import UserModel, BusinessModel, IndividualModel

from config import db 

from flask_restful import Resource
from flask import session, make_response, request

class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in UserModel.query.all()]
        return users, 201
    
class BusinessList(Resource):
    def post(self):
        json = request.get_json()
        
        account_type = json.get("ac_type")

        if account_type=="business":
            new_business = BusinessModel(
                email=json.get("email"),
                ac_type=account_type,
                name=json.get("name"),
                postal_code=json.get("postal_code"),
                district_block=json.get("district_block"),
                building_name=json.get("building_name"),
                floor_room=json.get("floor_room"),
                allow_email=json.get("allow_email"),
                city_id=json.get("city_id")
            )
            db.session.add(new_business)
            db.session.commit()
            return new_business.to_dict(), 201
        else:
            return{"message": "User is not a business. Sign up failed"}