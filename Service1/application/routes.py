from application import app
from flask import render_template, request
import requests

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://sfia2project_service4_1:5003/theme')
    print(response)
    sentence = response.text
    return render_template('index.html', sentence = sentence, title = 'Home')

# can easily use a random number generator to pick which implementation to use