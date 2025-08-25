from config import db

from models.individual_wishlist import IndividualWishlistModel

from flask_restful import Resource
from flask import session, request, make_response

class IndividualWishList(Resource):
    def post(self):
        json = request.get_json()

        try:
            new_wishlist = IndividualWishlistModel(
                individual_id=json.get("individual_id"),
                business_id=json.get("business_id")
            )
            db.session.add(new_wishlist)
            db.session.commit()
            return new_wishlist.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}, 401