from dao.model.director import Director
from marshmallow import Schema, fields


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()



