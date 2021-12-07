from dao.model.genre import GenreSchema
from flask_restx import Resource, Namespace
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        genres_ = genres_schema.dump(genres)
        return genres_, 200


@genre_ns.route('/<id>')
class GenreView(Resource):
    def get(self, id: int):
        genre = genre_service.get_one(id)
        genre_ = genre_schema.dump(genre)
        return genre_, 200
