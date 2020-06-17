from app import db, app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviedb.db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

favorite = db.Table('favorite',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer)
    fav_movies = db.relationship('User', secondary=favorite, backref=db.backref('movies', lazy='dynamic'))

    def __init__(self, title, year):
        self.title = title
        self.year = year