from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet (db.Model):
    """Pet Model"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(
        db.String, default='https://cdn.pixabay.com/photo/2016/07/21/14/18/dog-1532627__340.png')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} photo_url={p.photo_url}age={p.age} notes={p.notes} available={p.available} >"
