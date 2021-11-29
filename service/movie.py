from dao.model.movie import Movie
from dao.movie import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self):
        return self.movie_dao.get_all()

    def create(self, new_movie):
        return self.movie_dao.create(new_movie=new_movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid=mid)

    def update(self, movie):
        movie = Movie(**movie)
        return self.movie_dao.update(movie)
