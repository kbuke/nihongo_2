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
        user_info = IndividualModel.query.filter(IndividualModel.id==user_id).first()
        user_info = user_info.to_dict()

        existing_wishlists = [wishlist["name"] for wishlist in user_info["wishlists"]]
        print(existing_wishlists)

        wishlist_name = f"{json.get('name')} Prefecture"

        if wishlist_name in existing_wishlists:
            return{"error": f"This user has already created a wishlist for {wishlist_name}"}, 422
        else:
            wishlist_name=wishlist_name

        try:
            new_wishlist = WishlistModel(
                name=wishlist_name,
                img=json.get("img"),
                description=json.get("description"),
                individual_id=user_id
            )
            db.session.add(new_wishlist)
            db.session.commit()
            return new_wishlist.to_dict(), 201 
        except ValueError as e:
            return {"message": [str(e)]}
        

