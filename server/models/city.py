# try and see if we can add a recommended_length to show how long people usually stay in this city
# my idea for this is:
    # on the review model add a column showing recommended no. of days


from config import db
from sqlalchemy_serializer import SerializerMixin

class CityModel(db.Model, SerializerMixin):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    population = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)

    # Set up relationships
        # one-to-many, where cities are the many
    prefecture_id = db.Column(db.ForeignKey("prefectures.id"))
    prefecture = db.relationship("PrefectureModel", back_populates="cities")
        # one-to-many where cities are the one
    businesses = db.relationship("BusinessModel", back_populates="city", lazy="dynamic")
    sites = db.relationship("SiteModel", back_populates="city", lazy="dynamic")
        # many-to-many
    wishlist = db.relationship("WishlistModel", back_populates="city", secondary="location_business_wishlists")

    # serialise rules
    serialize_rules = (
        "-prefecture.cities",
        "-prefecture.wishlist",
        "-prefecture.capital",
        "-prefecture.intro",

        "-businesses.city",
        "-businesses.wishlist",
        "-businesses.district_block",
        "-businesses.email",
        "-businesses.ac_type",
        "-businesses.city_id",
        "-businesses.floor_room",
        "-businesses.postal_code",
        "-businesses.building_name",
        "-businesses.allow_email",

        "-wishlist",

        "-sites.city",
        "-sites.wishlist",
        "-sites.city_id",
    )
