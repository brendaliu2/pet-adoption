"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):

    name = StringField('Name:', validators=[InputRequired()])
    species = StringField('Species:', validators=[InputRequired()])
    photo_url = StringField('Photo URL:', validators=[InputRequired()])
    age = SelectField('Age:', choices=[('baby','Baby'),
                                       ('young','Young'),
                                       ('adult','Adult'),
                                       ('senior','Senior')])
                    # Way to force user to actively select?
    notes = StringField('Notes:', validators=[Optional()])
    
    def validate_name(form, field):
        if len(field.data) > 5:
            raise ValidationError('Shorter input please!')