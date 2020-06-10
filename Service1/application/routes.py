from flask import render_template, request
from application import app, db
from application.models import Stories
from application.forms import StoryForm
import requests

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://sfia2project_service4_1:5003/theme')
# can easily use a random number generator to pick which implementation to use    
#    print(response)
    sentence = response.text

    story_form = StoryForm()
    if story_form.validate_on_submit():
        storyData = Meals(
            author = story_form.author.data,
            title = story_form.title.data,
            story = story_form.story.data,
            keywords = sentence
        )

        db.session.add(storyData) 
        db.session.commit()

        return redirect(url_for('stories'))


    return render_template('index.html', sentence = sentence, title = 'Home')



@app.route('/stories')
def stories():
    storyData =Stories.query.all()
    return render_template('stories.html', title="Stories", stories=storyData)


# Edit functionality
# <a href="edit_story/{{story.id}}">Edit story</a>
# Need to store the keywords in database likely as a string of words. This will lead to duplication of words
# Alternatively you could use relational database
# Table of setting, noun and theme. Story will then have 3 foreign keys (many-one relationship)
# not part of the mvp 