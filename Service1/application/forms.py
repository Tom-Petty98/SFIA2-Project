from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
# from application import db

class StoryForm(FlaskForm):
    author = StringField('Author Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    title = StringField('Title Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    story = TextAreaField('Write your story here',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit_story = SubmitField('Post Story!')