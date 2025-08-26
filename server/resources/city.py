from config import db

from models.city import CityModel

from flask_restful import Resource
from flask import session, request, make_response

class CityList(Resource):
    def get(self):
        cities = [city.to_dict() for city in CityModel.query.all()]
        return cities, 200
    
    def post(self):
        json = request.get_json()

        city_population = json.get("population")

        if type(city_population) is str:
            city_population = int(city_population)

            if 1000 <= city_population <= 999999:
                city_population=f"{round(city_population/1000, 2)} Thousand"
            elif 1000000 <= city_population <= 99999999:
                city_population=f"{round(city_population/1000000, 2)} Million"
            else:
                city_population=city_population
                
        else:
            if 1000 <= city_population <= 999999:
                city_population=f"{round(city_population/1000, 2)} Thousand"
            elif 1000000 <= city_population <= 99999999:
                city_population=f"{round(city_population/1000000, 2)} Million"
            else:
                city_population=city_population

        try:
            new_city = CityModel(
                name=json.get("name"),
                population=city_population,
                img=json.get("img"),
                prefecture_id=json.get("prefecture_id")
            )
            db.session.add(new_city)
            db.session.commit()
            return new_city.to_dict()
        except ValueError as e:
            return {"message": [str(e)]}

class City(Resource):
    def get(self, id):
        city = CityModel.query.filter(CityModel.id==id).first()
        if city:
            return make_response(city.to_dict(), 201)
        else:
            return{"message": f"City {id} not found"}, 404
    
    def patch(self, id):
        data = request.get_json()

        city = CityModel.query.filter(CityModel.id==id).first()

        if city:
            try:
                for attr in data:
                    setattr(city, attr, data[attr])
                db.session.add(city)
                db.session.commit()
                return make_response(city.to_dict())
            except ValueError as e:
                return {"message": [str(e)]}
        else:
            return {"message": f"City {id} not found"}, 404
    
    def delete(self, id):
        city = CityModel.query.filter(CityModel.id==id).first()
        if city:
            db.session.delete(city)
            db.session.commit()
            return {"message": f"City {id} deleted."}
        else:
            return {"message": f"City {id} not found."}, 404