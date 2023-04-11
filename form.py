from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, URLField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL, AnyOf


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Please add pet's name")])
    species = StringField("Species", validators=[
        InputRequired(message="Please add pet's species"), AnyOf(values=['cat', 'dog', 'porcupine'], message="cat, dog or porcupine only")])
    photo_url = StringField("URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("Availability")
