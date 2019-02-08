from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask 및 sqlalchemy 설정
# app.config('SQLALCHEMY_DATABASE_URI')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 및 migration 초기화
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    title_en = db.Column(db.String(80), unique=False)
    audience = db.Column(db.Integer, unique=False)
    open_date = db.Column(db.String(80), unique=False)
    genre = db.Column(db.String(80), unique=False)
    watch_grade = db.Column(db.String(80), unique=False)
    score = db.Column(db.Float, unique=False)
    poster_url = db.Column(db.TEXT, unique=False)
    description =  db.Column(db.TEXT, unique=False)
    
    def __init__(self, title, title_en, audience, open_date, genre, watch_grade, score, poster_url, description):
        self.title = title
        self.title_en = title_en
        self.audience = audience
        self.open_date = open_date
        self.genre = genre
        self.watch_grade = watch_grade
        self.score = score
        self.poster_url = poster_url
        self.description = description
    

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies = movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)