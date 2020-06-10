from application import db

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    story = db.Column(db.String(500), nullable=False, unique=True)
    keywords = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return ''.join([
             'Id: ', str(self.id), ' ', 'Story: ', self.story
            ])