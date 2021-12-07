from implemented import director_service
from dao.model.director import DirectorSchema
from flask_restx import Resource, Namespace


director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        directors_ = directors_schema.dump(directors)
        return directors_, 200


@director_ns.route('/<did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)
        director_ = directors_schema.dump(director)
        return director_, 200
