from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= str(getenv('STORYDBURI'))
app.config['SECRET_KEY'] = getenv('SECRETKEY')
db = SQLAlchemy(app)

from application import routes