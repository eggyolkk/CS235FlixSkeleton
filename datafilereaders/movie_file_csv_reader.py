import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = []
        self._dataset_of_actors = []
        self._dataset_of_directors = []
        self._dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                add_title = row['Title']
                add_year = int(row['Year'])
                add_movie = Movie(add_title, add_year)
                self._dataset_of_movies.append(add_movie)

                actors_list = row['Actors'].split(",")
                for a in actors_list:
                    actor = a.strip()
                    add_actor = Actor(actor)
                    if add_actor not in self._dataset_of_actors:
                        self._dataset_of_actors.append(add_actor)

                directors_list = row['Director'].split(",")
                for d in directors_list:
                    add_director = Director(d)
                    if add_director not in self._dataset_of_directors:
                        self._dataset_of_directors.append(add_director)

                genre_list = row['Genre'].split(",")
                for g in genre_list:
                    add_genre = Genre(g)
                    if add_genre not in self._dataset_of_genres:
                        self._dataset_of_genres.append(add_genre)

                index += 1

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres


