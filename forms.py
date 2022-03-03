from flask_wtf import Form
from wtforms import EmailField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class DeleteForm(Form):
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Delete Member')


class AddForm(Form):
    first_name = StringField('First Name',
                             validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name',
                            validators=[DataRequired(), Length(min=2, max=30)])
    facebook = StringField('Facebook',
                           validators=[])
    twitter = StringField('Twitter',
                          validators=[])
    party = StringField('Party',
                        validators=[DataRequired(), Length(min=2, max=50)])
    gov_role = StringField('Gov Role',
                           validators=[])
    knesset_role = StringField('Knesset Role',
                               validators=[])
    additional_role = StringField('Additional Role',
                                  validators=[])
    personal_phone = IntegerField('Personal Phone',
                                  validators=[])
    office_phone = IntegerField('Office Phone',
                                validators=[])
    email = EmailField('Email',
                       validators=[])
    speaker_name = StringField('Speaker Name',
                               validators=[])
    speaker_phone = IntegerField('Speaker Phone',
                                 validators=[])
    head_office_name = StringField('Head Office Name',
                                   validators=[])
    head_office_phone = IntegerField('Head Office Phone',
                                     validators=[])
    political_consultant_name = StringField('Political Consultant Name',
                                            validators=[])
    political_consultant_phone = IntegerField('Political Consultant Name',
                                              validators=[])
    picture = StringField('Picture (URL)',
                          validators=DataRequired())
    position = StringField('Position',
                           validators=DataRequired())

    submit = SubmitField('Add Member')
