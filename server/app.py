from config import api, app

from resources.prefecture import PrefectureList, Prefecture
from resources.city import CityList
from resources.user import UserList, User
from resources.sites import SitesList, Site
from resources.wishlist import WishlistList
from resources.location_business_wishlist import LocationBusinessWishlistList

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(Prefecture, "/prefectures/<int:id>")

api.add_resource(CityList, "/cities")

api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<int:id>")

api.add_resource(SitesList, "/sites")
api.add_resource(Site, "/sites/<int:id>")

api.add_resource(WishlistList, "/wishlists")

api.add_resource(LocationBusinessWishlistList, "/locationwishlists")

if __name__ == "__main__":
    app.run(port=5555, debug=True)