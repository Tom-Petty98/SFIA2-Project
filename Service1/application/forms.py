from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField
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
    keywords = HiddenField('Keywords',
        validators = [
            DataRequired(),
            Length(min=2, max=60)
        ]
    )
    submit_story = SubmitField('Post Story!')