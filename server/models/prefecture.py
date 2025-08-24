from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db

class PrefectureModel(db.Model, SerializerMixin):
    __tablename__ = "prefectures"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    img = db.Column(db.String, nullable=False)
    capital = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=False)

    # set up relationships
        # one-to-many (where prefecture is the one)
            # prefecture - cities
            # prefecture - businesses
            # prefecture - sites
        # one-to-many (where prefecture is the many)

        # many-to-many
            # user's wishlist
            # user's visited
            # user's reviews on categories