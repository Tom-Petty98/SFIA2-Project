from application import db
from application.models import Stories

db.drop_all()
db.create_all()