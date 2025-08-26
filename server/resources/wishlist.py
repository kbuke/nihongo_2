from config import db 

from flask import session, make_response, request
from flask_restful import Resource

from models.wishlist import WishlistModel
from models.prefecture import PrefectureModel
from models.user import IndividualModel

class WishlistList(Resource):
    def get(self):
        wishlists = [wishlist.to_dict() for wishlist in WishlistModel.query.all()]
        return wishlists
    
    def post(self):
        json = request.get_json()

        user_id = json.get("user_id")
        user_info = IndividualModel.query.filter(IndividualModel.id == user_id).first()
        if user_info:
            user_info = user_info.to_dict()
        else:
            return {"error": "No user found"}
        print(user_info)

        try:
            new_wishlist = WishlistModel(
                name=json.get("name"),
                img=json.get("img"),
                description=json.get("description"),
                individual_id=user_id
            )
            db.session.add(new_wishlist)
            db.session.commit()
            return new_wishlist.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}
        

