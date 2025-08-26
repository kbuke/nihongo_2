from config import db 

from sqlalchemy_serializer import SerializerMixin

class SiteModel(db.Model, SerializerMixin):
    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    img = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=False)

    # set up relationships
        # one-to-many where sites are the many
    city_id = db.Column(db.ForeignKey("cities.id"))
    city = db.relationship("CityModel", back_populates="sites")
        # many-to-many relationships
    wishlist = db.relationship("WishlistModel", back_populates="site", secondary="location_business_wishlists")
    
    # serialise rules
    serialize_rules = (
        "-city.sites",
        "-city.wishlist",
        "-city.businesses",
        "-city.prefecture.intro",
        "-city.prefecture.capital",
        "-city.population",
        

        "-wishlist",
    )