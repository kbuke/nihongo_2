from models.location_business_wishlist import LocationBusinessWishListModel

from flask_restful import Resource

from flask import session, make_response, request

from config import db

class LocationBusinessWishlistList(Resource):
    def post(self):
        json=request.get_json()

        business_id = json.get("business_id")
        sites_id = json.get("sites_id")

        if business_id and not sites_id:
            try:
                new_wishlist_item = LocationBusinessWishListModel(
                    business_id=business_id,
                    sites_id=None,
                    wishlist_id=json.get("wishlist_id")
                )
                db.session.add(new_wishlist_item)
                db.session.commit()
                return new_wishlist_item.to_dict(), 201
            except ValueError as e:
                return {"message": [str(e)]}
            
        elif not business_id and sites_id:
            try:
                new_wishlist_item = LocationBusinessWishListModel(
                    business_id=None,
                    sites_id=sites_id,
                    wishlist_id=json.get("wishlist_id")
                )
                db.session.add(new_wishlist_item)
                db.session.commit()
                return new_wishlist_item.to_dict(), 201
            except ValueError as e:
                return {"message": [str(e)]}
        else:
            return{"message": "Must either have a business or site id"}, 422
