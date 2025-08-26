from config import db 

from sqlalchemy_serializer import SerializerMixin

class BusinessInterestModel(db.Model, SerializerMixin):
    __tablename__ = "business_interests"

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"))
