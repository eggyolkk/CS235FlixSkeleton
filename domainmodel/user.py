class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name: str = user_name.strip().lower()
        self.__password: str = password
        self.__watched_movies: list = []
        self.__reviews: list = []
        self.__time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> str:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self) -> str:
        repr_string = "<User " + str(self.__user_name) + ">"
        return repr_string

    def __eq__(self, other) -> bool:
        return self.__user_name == other.__user_name

    def __lt__(self, other) -> bool:
        return self.__user_name < other.__user_name

    def __hash__(self) -> str:
        unique_id = str(self.__user_name) + str(self.__password)
        return hash(unique_id)

    def watch_movie(self, movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        self.__reviews.append(review)