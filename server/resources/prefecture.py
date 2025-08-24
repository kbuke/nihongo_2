from config import db 

from models.prefecture import PrefectureModel

from flask_restful import Resource
from flask import session, request, make_response

class PrefectureList(Resource):
    def get(self):
        prefectures = [prefecture.to_dict() for prefecture in PrefectureModel.query.all()]
        return prefectures, 200