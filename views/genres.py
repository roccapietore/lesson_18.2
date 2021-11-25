from models import Genre, GenreSchema
from flask_restx import Resource, Namespace


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = Genre.query.all()
        genres_ = genres_schema.dump(genres)
        return genres_, 200


@genre_ns.route('/<id>')
class GenreView(Resource):
    def get(self, id: int):
        genre = Genre.query.get(id)
        genre_ = genre_schema.dump(genre)
        return genre_, 200
