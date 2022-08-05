from models import Pet, db

from app import app

db.drop_all()
db.create_all()

fluffy = Pet(name = "Fluffy",
              species = "Cat",
              photo_url = "https://cdn.britannica.com/91/181391-050-1DA18304/cat-toes-paw-number-paws-tiger-tabby.jpg?q=60",
              age = "young",
              available = True)


fluffy2 = Pet(name = "Fluffy2",
              species = "Cat",
              photo_url = "https://cdn.britannica.com/91/181391-050-1DA18304/cat-toes-paw-number-paws-tiger-tabby.jpg?q=60",
              age = "young",
              available = False)


db.session.add(fluffy)
db.session.add(fluffy2)

db.session.commit()