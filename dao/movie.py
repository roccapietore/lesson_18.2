from dao.model.movie import Movie
from marshmallow import Schema, fields


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def get_all(self, movie):
        new_movie = Movie(**movie)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def delete(self, id):
        movie = self.get_one(id=id)
        self.session.delete(movie)
        self.session.commit()


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


