from config import db

from models.individual_wishlist import IndividualWishlistModel

from flask_restful import Resource
from flask import session, request, make_response

class IndividualWishList(Resource):
    def post(self):
        json = request.get_json()

        business_id = json.get("business_id")
        sites_id = json.get("sites_id")

        breakpoint()

        if business_id or sites_id:
            if business_id:
                new_wishlist = IndividualWishlistModel(
                    individual_id=json.get("individual_id"),
                    business_id=json.get("business_id")
                )
                db.session.add(new_wishlist)
                db.session.commit()
                return new_wishlist.to_dict(), 201
            
            else:
                new_wishlist = IndividualWishlistModel(
                    individual_id=json.get("individual_id"),
                    sites_id=json.get("sites_id")
                )
                db.session.add(new_wishlist)
                db.session.commit()
                return new_wishlist.to_dict(), 201
        else:
            return {"message": "You must enter either a site or business id"}, 422

        # try:
        #     new_wishlist = IndividualWishlistModel(
        #         individual_id=json.get("individual_id"),
        #         business_id=json.get("business_id")
        #     )
        #     db.session.add(new_wishlist)
        #     db.session.commit()
        #     return new_wishlist.to_dict(), 201
        # except ValueError as e:
        #     return {"message": [str(e)]}, 401