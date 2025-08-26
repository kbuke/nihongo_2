# Interests will be what people look for in a holiday.
    # history, beach, party etc
# It will have a many-to-many relationship with indiviuals
    # individuals can be interest in many things
    # and things can be liked by many individuals
# Businesses and sites will also mention what interests they fulfill.
# It is another example of many-to-many relationships
    # A site can have many interests it fulfills
    # An interest can belong to many sites

from sqlalchemy_serializer import SerializerMixin
from config import db 

class InterestModel(db.Model, SerializerMixin):
    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String, nullable=False, unique=True)
    img = db.Column(db.String, nullable=False, unique=True)

    # set up relations
    individual = db.relationship("IndividualModel", back_populates="interests", secondary="individual_interests")