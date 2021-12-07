from dao.movie import MovieDao


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.movie_dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.movie_dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.movie_dao.get_by_year(filters.get("year"))
        else:
            movies = self.movie_dao.get_all()
        return movies

    def create(self, new_movie):
        return self.movie_dao.create(new_movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid)

    def update(self, movie_d):
        self.movie_dao.update(movie_d)
        return self.movie_dao
