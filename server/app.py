from config import api, app

from resources.prefecture import PrefectureList, Prefecture
from resources.city import CityList
from resources.user import UserList
from resources.individual_wishlist import IndividualWishList
from resources.sites import SitesList

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(Prefecture, "/prefectures/<int:id>")

api.add_resource(CityList, "/cities")

api.add_resource(UserList, "/users")

api.add_resource(IndividualWishList, "/wishlists")

api.add_resource(SitesList, "/sites")

if __name__ == "__main__":
    app.run(port=5555, debug=True)