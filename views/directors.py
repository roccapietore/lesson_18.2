from models import Director, DirectorSchema
from flask_restx import Resource, Namespace


director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        directors_ = directors_schema.dump(directors)
        return directors_, 200


@director_ns.route('/<id>')
class DirectorView(Resource):
    def get(self, id: int):
        director = Director.query.get(id)
        director_ = directors_schema.dump(director)
        return director_, 200
