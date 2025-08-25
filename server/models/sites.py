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

    # serialise rules
    serialize_rules = (
        "-city.sites",
    )