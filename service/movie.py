from flask_restx import reqparse, Namespace


from dao.model.movie import Movie
from dao.movie import MovieDao


parser = reqparse.RequestParser()
parser.add_argument("director_id", type=int)
parser.add_argument("genre_id", type=int)

movie_ns = Namespace('movies')


class MovieService:
    def __init__(self, movie_dao: MovieDao):
        self.movie_dao = movie_dao

    @movie_ns.expect(parser)
    def get_one(self):
        movies_director = parser.parse_args()["director_id"]
        movies_genre = parser.parse_args()["genre_id"]
        if movies_director and movies_genre:  # поиск фильмов по режиссеру и жанру
            filtered_movies = Movie.query.filter_by(director_id=movies_director, genre_id=movies_genre).all()

        elif movies_genre:  # поиск фильмов по жанру
            filtered_movies = Movie.query.filter_by(genre_id=movies_genre).all()

        elif movies_director:  # поиск фильмов по режиссеру
            filtered_movies = Movie.query.filter_by(director_id=movies_director).all()

        else:  # вывод всех фильмов
            filtered_movies = Movie.query.all()

        return self.movie_dao.get_one(filtered_movies)

    def get_all(self):
        return self.movie_dao.get_all()

    def create(self, new_movie):
        return self.movie_dao.create(new_movie=new_movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid=mid)

    def update(self, movie):
        movie = Movie(**movie)
        return self.movie_dao.update(movie)
