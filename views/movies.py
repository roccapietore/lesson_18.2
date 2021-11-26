from flask import request

from dao.movie import Movie, MovieSchema
from flask_restx import Resource, reqparse, Namespace, Api
from setup import db


movie_ns = Namespace('movies')

parser = reqparse.RequestParser()
parser.add_argument("director_id", type=int)
parser.add_argument("genre_id", type=int)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):

    @movie_ns.expect(parser)
    def get(self):
        movies_director = parser.parse_args()["director_id"]
        movies_genre = parser.parse_args()["genre_id"]

        if movies_director and movies_genre:  # поиск фильмов по режиссеру и жанру
            filtered_movies = Movie.query.filter_by(director_id=movies_director, genre_id=movies_genre).all()

        elif movies_genre:  # поиск фильмов по жанру
            filtered_movies = Movie.query.filter_by(genre_id=movies_genre).all()

        elif movies_director:  # поиск фильмов по режиссеру
            filtered_movies = Movie.query.filter_by(director_id=movies_director).all()

        else:  # вывод всех фильмов
            filtered_movies = Movie.query.all()

        if not filtered_movies:
            return "", 404

        movies = movies_schema.dump(filtered_movies)
        return movies, 200

    def post(self):
        req_json = request.json
        new_movies = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movies)
        return "", 201


@movie_ns.route("/<id>")
class MovieView(Resource):
    def get(self, id: int):
        movie = Movie.query.get(id)
        if not movie:
            return "", 404
        get_movie = movie_schema.dump(movie)
        return get_movie, 200

    def put(self, id: int):
        movie = Movie.query.get(id)
        if not movie:
            return "", 404
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, id: int):
        movie = Movie.query.get(id)
        if not movie:
            return "", 404
        db.session.delete(movie)
        db.session.commit()
        return "", 204

