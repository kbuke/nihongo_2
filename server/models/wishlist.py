# A wishlist belongs to one user, however a user can have many wishlists
    # Therefore it is a one-to-many relationship with users

# A prefecture, city, neighbourhood, business or site can belong to many wishlists
# Many prefectures, cities, neighbourhoods, businesses or sites can belong to a wishlist
    # Therefore it has a many-to-many relationship with these models

from config import db

from sqlalchemy_serializer import SerializerMixin

class WishlistModel(db.Model, SerializerMixin):
    __tablename__ = "wishlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) # it should be unique to the user, ie no two of the same for same user
    img = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Set up relations
        # one-to-many
    individual_id = db.Column(db.ForeignKey("individuals.id"))
    individual = db.relationship("IndividualModel", back_populates="wishlists")
        # many-to-many
    prefecture = db.relationship("PrefectureModel", back_populates="wishlist", secondary="location_business_wishlists")
    city = db.relationship("CityModel", back_populates="wishlist", secondary="location_business_wishlists")
    business = db.relationship("BusinessModel", back_populates="wishlist", secondary="location_business_wishlists")
    site = db.relationship("SiteModel", back_populates="wishlist", secondary="location_business_wishlists")

    serialize_rules = (
        # "-individual",
        "-prefecture.wishlist",
        "-city",
        "-business",
        "-site",
        # "-individual.wishlists",
        # "-individual.prefecture",
        # "-individual.city",
        # "-individual.business",
        # "-individual.site",

        # "-prefecture.wishlist",
        # "-prefecture.city",
        # "-prefecture.business",
        # "-prefecture.site",
        # "-prefecture.individual",

        # "-city.wishlist",
        # "-city.prefecture",
        # "-city.business",
        # "-city.site",
        # "-city.individual",

        # "-business.wishlist",
        # "-business.prefecture",
        # "-business.city",
        # "-business.site",
        # "-business.individual",

        # "-site.wishlist",
        # "-site.prefecture",
        # "-site.city",
        # "-site.business",
        # "-site.individual",
    )