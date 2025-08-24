from config import api, app

from resources.prefecture import PrefectureList, Prefecture

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(Prefecture, "/prefectures/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)