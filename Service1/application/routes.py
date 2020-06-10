from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Stories
from application.forms import StoryForm
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://sfia2-project_service4_1:5003/theme')
# can easily use a random number generator to pick which implementation to use    
#    print(response)
    sentence = response.text
    keywords = sentence.split(', ')

    story_form = StoryForm()
    if story_form.validate_on_submit():
        storyData = Stories(
            author = story_form.author.data,
            title = story_form.title.data,
            story = story_form.story.data,
            keywords = story_form.keywords.data
        )
        db.session.add(storyData) 
        db.session.commit()
        return redirect(url_for('stories'))
        
    elif request.method == 'GET':
        story_form.keywords.data = sentence


    return render_template('index.html', keywords = keywords, title = 'Home', story_form=story_form)


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

@app.route('/delete_story/<int:id>', methods=['GET', 'POST'])
def delete_meal(id):
    story = Stories.query.filter_by(id=id).first()
    db.session.delete(story)
    db.session.commit()
    return redirect(url_for('stories'))