from flask import request
from dao.model.movie import MovieSchema
from flask_restx import Resource, Namespace
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        movies = movies_schema.dump(all_movies)
        return movies, 200

    def post(self):
        req_json = request.json
        posted_movie = movie_service.create(req_json)
        return "", 201,  {"location": f"/movies/{posted_movie.id}"}


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        get_movie = movie_schema.dump(movie)
        return get_movie, 200

    def put(self, mid: int):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "", 204

