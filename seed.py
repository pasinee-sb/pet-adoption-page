from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()


p1 = Pet(name="Dino", species="dinosaur", photo_url="https://cdn.pixabay.com/photo/2015/12/08/22/45/dinosaur-1083924__340.jpg",
         age=5)
p2 = Pet(name="Bilbo", species="cat", photo_url="https://cdn.pixabay.com/photo/2023/04/07/07/14/cat-7905702__340.jpg",
         age=5)
p3 = Pet(name="Wilma", species="dog", photo_url="https://media.istockphoto.com/id/1160123255/photo/a-puppy-chocolate-brown-labrador.jpg?b=1&s=170667a&w=0&k=20&c=cS_1H72znlYLDGRWt0lOorUNMC6Ilx2Nq2ZoNrh9fq0=",
         age=5)
p4 = Pet(name="Bina", species="dog", photo_url="https://cdn.pixabay.com/photo/2018/01/09/11/04/dog-3071334__340.jpg",
         age=5)
p5 = Pet(name="Phoebe", species="lama", photo_url="https://media.istockphoto.com/id/656551516/photo/alpaca-white-ilama.jpg?b=1&s=170667a&w=0&k=20&c=NILrNewBvDkPQJXeFhq1bJLSjk6PQkxMXNvAZtEZOmo=",
         age=5)
p6 = Pet(name="Walla", species="rabbit", photo_url="https://media.istockphoto.com/id/1427343658/photo/a-gray-rabbit-with-ears-in-a-half-lop-position.jpg?b=1&s=170667a&w=0&k=20&c=ekqpemrswH-4LYMLJvUonaRH5b8nDVllKGJL5zfxeXc=",
         age=5)


db.session.add_all([p1, p2, p3, p4, p5, p6])
db.session.commit()
