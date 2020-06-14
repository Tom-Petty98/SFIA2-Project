from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Stories
from application.forms import StoryForm
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    response = requests.get('http://service4:5003/theme')
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

@app.route('/edit_story/<int:id>', methods=['GET', 'POST'])
def edit_story(id):
    story = Stories.query.filter_by(id=id).first()
    keywords = story.keywords.split(', ')

    story_form = StoryForm()
    if story_form.validate_on_submit():
        
        story.author = story_form.author.data
        story.title = story_form.title.data
        story.story = story_form.story.data
        story.keywords = story_form.keywords.data        
        db.session.commit()
        return redirect(url_for('stories'))

    elif request.method == 'GET':
        story_form.author.data = story.author
        story_form.title.data = story.title
        story_form.story.data = story.story
        story_form.keywords.data = story.keywords

    return render_template('edit_story.html', keywords = keywords, title = 'Edit story', story_form=story_form)


@app.route('/delete_story/<int:id>', methods=['GET', 'POST'])
def delete_story(id):
    story = Stories.query.filter_by(id=id).first()
    db.session.delete(story)
    db.session.commit()
    return redirect(url_for('stories'))