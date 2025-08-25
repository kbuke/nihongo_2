from config import db 

from flask import session, make_response, request
from flask_restful import Resource

from models.sites import SiteModel
from models.city import CityModel

class SitesList(Resource):
    def post(self):
        json = request.get_json()

        city_id = json.get("city_id")
        city = CityModel.query.filter(CityModel.id==city_id).first()

        if city:
            city_id = city_id
        else:
            return {"message": f"No city with id: {city_id} found"}, 422
        
        try:
            new_site = SiteModel(
                name=json.get("name"),
                img = json.get("img"),
                intro = json.get("intro"),
                city_id = city_id
            )
            db.session.add(new_site)
            db.session.commit()
            return new_site.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}