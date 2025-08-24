from config import api, app
from resources.prefecture import PrefectureList

api.add_resource(PrefectureList, "/prefectures")

if __name__ == "__main__":
    app.run(port=5555, debug=True)