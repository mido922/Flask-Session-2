from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    numberOfPages = db.Column(db.Integer)
    bookDescription = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

def __str__(self):
    return self.name

@classmethod
def get_all_objects(cls):
    return cls.query.all()