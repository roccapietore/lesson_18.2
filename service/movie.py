class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_one(self, id):
        return self.movie_dao.get_one(id)

    def get_all(self):
        return self.movie_dao.get_all()
