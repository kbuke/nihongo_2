from config import db 

from sqlalchemy_serializer import SerializerMixin

class IndividualWishlistModel(db.Model, SerializerMixin):
    __tablename__ = "individual_wishlists"

    id = db.Column(db.Integer, primary_key=True)
    individual_id = db.Column(db.Integer, db.ForeignKey("individuals.id"))
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))
