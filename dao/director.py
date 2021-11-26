from dao.model.director import Director


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Director).get(id)

    def get_all(self):
        return self.session.query(Director).all()
