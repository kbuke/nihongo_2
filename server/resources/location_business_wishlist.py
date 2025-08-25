from models.location_business_wishlist import LocationBusinessWishListModel

from flask_restful import Resource

from flask import session, make_response, request

from config import db

class LocationBusinessWishlistList(Resource):
    def post(self):
        json=request.get_json()

        wishlist_id = json.get("wishlist_id")
        prefecture_id = json.get("prefecture_id")
        city_id = json.get("city_id")
        business_id = json.get("business_id")
        sites_id = json.get("sites_id")

        if wishlist_id and prefecture_id and city_id:
            if business_id or sites_id:
                new_wishlist_item = LocationBusinessWishListModel(
                    prefecture_id=prefecture_id,
                    city_id=city_id,
                    business_id=business_id,
                    sites_id=sites_id,
                    wishlist_id=wishlist_id
                )
                db.session.add(new_wishlist_item)
                db.session.commit()
                return new_wishlist_item.to_dict(), 201
            else:
                return {"message": "Need either a business or site id"}, 422
        else:
            return{"message": "Must include a wishlist, city and prefecture id"}, 422
