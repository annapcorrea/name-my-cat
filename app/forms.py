from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    cat_name = StringField('Cat Name', validators=[DataRequired(), Length(min=2, max=64)])
    user_name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=64)])
    submit = SubmitField('Submit')
