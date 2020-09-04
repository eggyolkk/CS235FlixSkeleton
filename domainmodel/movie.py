from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, movie_title: str, release_date: int):
        if movie_title == "" or type(movie_title) is not str:
            self.__movie_title = None
        else:
            self.__movie_title: str = movie_title.strip()

        self.__release_date: int = release_date
        self.__description: str = None
        self.__director: Director = Director("")
        self.__actors: list = []
        self.__genres: list = []
        self.__runtime_minutes: int = None


    @property
    def title(self) -> str:
        return str(self.__movie_title)

    @property
    def release_date(self) -> int:
        return str(self.__release_date)

    @property
    def description(self) -> str:
        return str(self.__description)

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @title.setter
    def title(self, title):
        self.__title = title

    @release_date.setter
    def release_date(self, release_date):
        if release_date >= 1900:
            self.__release_date = release_date

    @description.setter
    def description(self, description):
        self.__description = description.strip()

    @director.setter
    def director(self, director):
        self.__director = director

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError

    def __repr__(self) -> str:
        reprstring = "<Movie " + self.__movie_title + ", " + str(self.__release_date) + ">"
        return reprstring

    def __eq__(self, other) -> bool:
        if self.title == other.title and self.__release_date == other.release_date:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.title < other.title:
            return True
        elif self.title == other.title and self.__release_date < other.release_date:
            return True
        else:
            return False

    def __hash__(self) -> str:
        unique_movie = str(self.__movie_title) + str(self.__release_date)
        return hash(unique_movie)

    def add_actor(self, actor):
        if actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)