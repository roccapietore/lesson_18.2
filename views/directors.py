from models import Director
from flask_restx import Resource, Namespace


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors, 200


@director_ns.route('/<id>')
class DirectorView(Resource):
    def get(self, id: int):
        director = Director.query.get(id)
        return director, 200
