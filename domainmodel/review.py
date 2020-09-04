from datetime import datetime
from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie: Movie = movie

        if 1 <= rating <= 10:
            self.__rating: int = rating
        else:
            self.__rating = None

        self.__review_text: str = review_text
        self.__timestamp: datetime = datetime.today()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self) -> str:
        reprstring = str(self.__movie) + ", " + str(self.__timestamp)
        return reprstring

    def __eq__(self, other) -> bool:
        if self.__review_text == other.review_text and self.__movie == other.movie and self.__rating == other.rating and self.__timestamp == other.timestamp:
            return True
        else:
            return False
