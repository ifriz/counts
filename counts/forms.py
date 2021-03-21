from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class CountsForm(FlaskForm):
    channel = StringField('Channel', validators=[DataRequired()])
    description = StringField('Description', widget=TextArea())