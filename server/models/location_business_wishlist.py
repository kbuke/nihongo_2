from config import db 

from sqlalchemy_serializer import SerializerMixin

class LocationBusinessWishListModel(db.Model, SerializerMixin):
    __tablename__ = "location_business_wishlists"

    id = db.Column(db.Integer, primary_key=True)
    prefecture_id = db.Column(db.Integer, db.ForeignKey("prefectures.id"), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"), nullable=True)
    sites_id = db.Column(db.Integer, db.ForeignKey("sites.id"), nullable=True)
    wishlist_id = db.Column(db.Integer, db.ForeignKey("wishlists.id"), nullable=False)