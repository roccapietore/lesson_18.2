from dao.model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, dir_id):
        return self.session.query(Movie).filter(Movie.director_id == dir_id).all()

    def get_by_genre_id(self, gen_id):
        return self.session.query(Movie).filter(Movie.genre_id == gen_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, movie):
        new_movie = Movie(**movie)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        updated_movie = self.get_one(movie.get("id"))
        updated_movie.title = movie.get("title")
        updated_movie.description = movie.get("description")
        updated_movie.trailer = movie.get("trailer")
        updated_movie.year = movie.get("year")
        updated_movie.rating = movie.get("rating")
        updated_movie.genre_id = movie.get("genre_id")
        updated_movie.director_id = movie.get("director_id")

        self.session.add(updated_movie)
        self.session.commit()


