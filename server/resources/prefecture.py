from config import db 

from models.prefecture import PrefectureModel

from flask_restful import Resource
from flask import session, request, make_response

class PrefectureList(Resource):
    def get(self):
        prefectures = [prefecture.to_dict() for prefecture in PrefectureModel.query.all()]
        return prefectures, 200
    
    def post(self):
        json = request.get_json()

        try:
            new_prefecture = PrefectureModel(
                name=json.get("name"),
                img=json.get("img"),
                capital=json.get("capital"),
                intro=json.get("intro")
            )
            db.session.add(new_prefecture)
            db.session.commit()
            return new_prefecture.to_dict(), 201
        except ValueError as e:
            return {"message": [str(e)]}, 404