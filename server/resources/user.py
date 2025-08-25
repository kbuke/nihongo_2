from models.user import UserModel, BusinessModel, IndividualModel

from models.city import CityModel

from config import db 

from flask_restful import Resource
from flask import session, make_response, request

class UserList(Resource):
    def get(self):
        users = [user.to_dict() for user in UserModel.query.all()]
        return users, 201
    
    def post(self):
        json=request.get_json()

        account_type = json.get("ac_type")

        city_id = json.get("city_id")
        city = CityModel.query.filter(CityModel.id==city_id).first()
        print(city)

        if account_type=="business" and city:
            new_business = BusinessModel(
                email=json.get("email"),
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
        
        elif city==None:
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
    
# class BusinessList(Resource):
#     def post(self):
#         json = request.get_json()
        
#         account_type = json.get("ac_type")

#         if account_type=="business":
#             new_business = BusinessModel(
#                 email=json.get("email"),
#                 ac_type=account_type,
#                 name=json.get("name"),
#                 postal_code=json.get("postal_code"),
#                 district_block=json.get("district_block"),
#                 building_name=json.get("building_name"),
#                 floor_room=json.get("floor_room"),
#                 allow_email=json.get("allow_email"),
#                 city_id=json.get("city_id")
#             )
#             db.session.add(new_business)
#             db.session.commit()
#             return new_business.to_dict(), 201
#         else:
#             return{"message": "User is not a business. Sign up failed"}