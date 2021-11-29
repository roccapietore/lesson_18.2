from flask import Flask
from flask_restx import Api

from dao.director import Director
from dao.genre import Genre
from dao.movie import Movie
from setup import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from config import Config
from data import data

config = Config()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()
        for movie in data["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            with db.session.begin():
                db.session.add(m)

        for director in data["directors"]:
            d = Director(

                name=director["name"],
            )
            with db.session.begin():
                db.session.add(d)

        for genre in data["genres"]:
            d = Genre(

                name=genre["name"],
            )
            with db.session.begin():
                db.session.add(d)


app = create_app()
app.debug = True
create_data(app, db)

if __name__ == '__main__':
    app.run(host="localhost", port=10007, debug=True)

