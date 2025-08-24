from config import api, app

from resources.prefecture import PrefectureList, Prefecture
from resources.city import CityList

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(Prefecture, "/prefectures/<int:id>")

api.add_resource(CityList, "/cities")

if __name__ == "__main__":
    app.run(port=5555, debug=True)