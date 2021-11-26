from dao.model.genre import Genre
from marshmallow import Schema, fields


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Genre).get(id)

    def get_all(self):
        return self.session.query(Genre).all()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

