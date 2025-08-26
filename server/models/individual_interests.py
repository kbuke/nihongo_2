from sqlalchemy_serializer import SerializerMixin
from config import db

class IndividualInterestsModel(db.Model, SerializerMixin):
    __tablename__ = "individual_interests"

    id = db.Column(db.Integer, primary_key=True)
    individual_id = db.Column(db.Integer, db.ForeignKey("individuals.id"))
    interests_id = db.Column(db.Integer, db.ForeignKey("interests.id"))