from models import Genre
from flask_restx import Resource, Namespace


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        return genres, 200


@genre_ns.route('/<id>')
class GenreView(Resource):
    def get(self, id: int):
        genre = Genre.query.get(id)
        return genre, 200
