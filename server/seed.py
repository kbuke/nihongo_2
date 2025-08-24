from models.prefecture import PrefectureModel

from app import app
from config import db 

if __name__ == "__main__":
    with app.app_context():
        print("Start seeding...")

        db.drop_all()
        db.create_all()

        print("Begin seeding...")

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

        print("Finished seeding.")