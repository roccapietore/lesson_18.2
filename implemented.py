from dao.director import DirectorDao
from dao.genre import GenreDao
from dao.movie import MovieDao
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup import db

director_dao = DirectorDao(session=db)
director_service = DirectorService(director_dao=director_dao)

genre_dao = GenreDao(session=db)
genre_service = GenreService(genre_dao=genre_dao)

movie_dao = MovieDao(session=db)
movie_service = MovieService(movie_dao=movie_dao)

