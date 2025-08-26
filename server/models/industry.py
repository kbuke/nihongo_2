from config import db 
from sqlalchemy_serializer import SerializerMixin

class IndustryModel(db.Model, SerializerMixin):
    __tablename__ = "industries"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    img = db.Column(db.String, nullable=False, unique=True)