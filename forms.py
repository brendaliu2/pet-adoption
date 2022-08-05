"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField, RadioField
from wtforms.validators import InputRequired, Optional, URL


DEFAULT_PIC = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJpBZicEZsc7y4DZoFhlFaRpOXWFu-Lcvdjg&usqp=CAU'
class AddPetForm(FlaskForm):
    """Add Pet Form"""

    name = SelectField('Name:', validators=[InputRequired()],
                        choices=[('cat','Cat'),
                                ('dog','Dog'),
                                ('porcupine','Porcupine')])
    species = StringField('Species:', validators=[InputRequired()])
    photo_url = StringField('Photo URL:', validators=[Optional(), URL()],
                            default = DEFAULT_PIC)
    age = SelectField('Age:', choices=[('baby','Baby'),
                                       ('young','Young'),
                                       ('adult','Adult'),
                                       ('senior','Senior')])
                    # Way to force user to actively select?
    notes = StringField('Notes:')


class EditPetForm(FlaskForm):
    """Edit Pet Form"""

    photo_url = StringField('Photo URL:', validators=[Optional(), URL()])
    notes = StringField('Notes:')
    available = BooleanField('Available:')




