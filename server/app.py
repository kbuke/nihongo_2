from config import api, app

from resources.prefecture import PrefectureList, Prefecture
from resources.city import CityList
from resources.user import UserList, User, IndividualList, Individual, BusinessList, Business
from resources.sites import SitesList, Site
from resources.wishlist import WishlistList
from resources.location_business_wishlist import LocationBusinessWishlistList
from resources.interests import InterestList
from resources.individual_interests import IndividualInterestLists, IndividualInterest
from resources.business_interests import BusinessInterestList
from resources.industry import IndustryList
from resources.business_industry import BusinessIndustryList

api.add_resource(PrefectureList, "/prefectures")
api.add_resource(Prefecture, "/prefectures/<int:id>")

api.add_resource(CityList, "/cities")

api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<int:id>")
api.add_resource(IndividualList, "/individuals")
api.add_resource(Individual, "/individuals/<int:id>")
api.add_resource(BusinessList, "/businesses")
api.add_resource(Business, "/businesses/<int:id>")

api.add_resource(SitesList, "/sites")
api.add_resource(Site, "/sites/<int:id>")

api.add_resource(WishlistList, "/wishlists")

api.add_resource(LocationBusinessWishlistList, "/locationwishlists")

api.add_resource(InterestList, "/interests")

api.add_resource(IndividualInterestLists, "/individualinterests")
api.add_resource(IndividualInterest, "/individualinterests/<int:id>")

api.add_resource(BusinessInterestList, "/businessinterests")

api.add_resource(IndustryList, "/industries")

api.add_resource(BusinessIndustryList, "/businessindustries")

if __name__ == "__main__":
    app.run(port=5555, debug=True)