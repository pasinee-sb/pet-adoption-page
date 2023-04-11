from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from form import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_me'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_pets():
    """show all pets"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """add pet to collection from form object made form.py"""
    form = AddPetForm()

    """if it is a post request and token is valid, pull data from form, add to database and render home page"""
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        """if no photo_url entered, get default value from model"""
        photo_url = photo_url if photo_url else None

        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        flash(
            f"Created new pet: name is {name}, species is {species}, age {age}** {notes}")
        return redirect('/')

    else:
        """if it is a get request or token is not valid, go to addpet form"""
        return render_template('addpet.html', form=form)


@app.route('/<int:pet_id>')
def show_detail(pet_id):
    """show each pet's info"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('petdetail.html', pet=pet)


@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """populate form with existing data"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    """if it is a post request and token is valid, pull data from form, update to database and render home page"""
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        # flash(f"Pet {{pet.name}} is updated")
        return redirect('/')

    else:
        return render_template('editpet.html', form=form)
