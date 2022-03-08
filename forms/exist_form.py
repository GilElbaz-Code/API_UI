from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ExistForm(Form):
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=30)])

    submit = SubmitField('Update Member')
