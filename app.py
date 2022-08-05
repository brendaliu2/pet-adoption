"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """Displays homepage"""

    pets = Pet.query.all()

    return render_template('home.html', pets = pets)

@app.route('/add', methods = ['GET','POST'])
def add_pet():
    """Handles add pet form and redirects back to home page if successful
        otherwise, rerender add form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes)

        db.session.add(new_pet)
        db.session.commit()

# flash message

        return redirect('/')

    else:
        return render_template('add.html', form=form)


@app.route('/<int:pet_id_number>', methods = ['GET','POST'])
def edit_pet(pet_id_number):
    """Handles edit pet form and redirects back to pet page if successful
        otherwise, rerender add form"""

    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        # eval converts return False string into boolean, is there another way?
        # eval huge security risk!!!

        db.session.commit()
        flash(f'Pet {pet.name} updated!')

        return redirect(f'/{pet_id_number}')

    else:
            return render_template('edit.html', form=form, pet=pet)





