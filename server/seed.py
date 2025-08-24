from models.prefecture import PrefectureModel
from models.city import CityModel
from models.user import IndividualModel, BusinessModel

from app import app
from config import db 

if __name__ == "__main__":
    with app.app_context():
        print("Start seeding...")

        db.drop_all()
        db.create_all()

        print("Begin seeding...")

        print("Seeing users...")
        kaan_buke=IndividualModel(
            email="kabuke13@gmail.com",
            ac_type="individual",
            first_name="Kaan",
            last_name="Buke",
            intro="I hope this works man"
        )
        db.session.add_all([kaan_buke])
        db.session.commit()
        print("Finished seeding users...")

        print("Seeding prefectures...")
        tokyo=PrefectureModel(
            name="Tokyo",
            img="Uploading later",
            capital="Tokyo",
            intro="The largest city in the world"
        )
        db.session.add_all([tokyo])
        db.session.commit()
        print("Finished seeding prefectures")

        print("Seeding cities...")
        tokyo_city=CityModel(
            name="Tokyo",
            population=37000000,
            img="Will upload at a later date",
            prefecture_id=1
        )
        db.session.add_all([tokyo_city])
        db.session.commit()
        print("Finished seeding cities.")

        print("Finished seeding.")