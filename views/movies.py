from flask import request
from dao.movie import Movie, MovieSchema
from flask_restx import Resource, Namespace
from implemented import movie_service


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self, filtered_movies):
        movies = movies_schema.dump(filtered_movies)
        return movies, 200

    def post(self):
        req_json = request.json
        posted_movie = movie_service.create(id)
        return "", 201


@movie_ns.route("/<id>")
class MovieView(Resource):
    def get(self, id: int):
        movie = movie_service.get_one(id)
        get_movie = movie_schema.dump(movie)
        return get_movie, 200

    def put(self, id: int):
        movie = movie_service.get_one(id)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        updated_movie = movie_service.update(movie)
        return "", 204

    def delete(self, id: int):
        movie = movie_service.delete(id)

        return "", 204

