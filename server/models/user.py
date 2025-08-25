from config import db

from sqlalchemy_serializer import SerializerMixin

class UserModel(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    ac_type = db.Column(db.String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": ac_type,
    }

class IndividualModel(UserModel):
    __tablename__ = "individuals"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=True)

    # set up relations
        # many-to-many
    businesses = db.relationship("BusinessModel", back_populates="individuals", secondary="individual_wishlists")
    sites = db.relationship("SiteModel", back_populates="individuals", secondary="individual_wishlists")

    # serialise rukes
    serialize_rules = (
        "-businesses.individuals",
    )

    __mapper_args__ = {
        "polymorphic_identity": "individual",
    }

class BusinessModel(UserModel):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    # set address columns
    postal_code=db.Column(db.String, nullable=False)
    district_block=db.Column(db.String, nullable=False)
    building_name=db.Column(db.String, nullable=True)
    floor_room=db.Column(db.String, nullable=True)

    allow_email = db.Column(db.Boolean, nullable=False)

    # set up relations
        # one-to-many w. businesses as the many
    city_id = db.Column(db.ForeignKey("cities.id"))
    city = db.relationship("CityModel", back_populates="businesses")
        # many-to-many 
    individuals = db.relationship("IndividualModel", back_populates="businesses", secondary="individual_wishlists")


    __mapper_args__ = {
        "polymorphic_identity": "business",
    }

    # serialise rules
    serialize_rules=(
        "-city.businesses",
    )