from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.watchlist import WatchList
from domainmodel.review import Review


class WatchingSimulation:
    def __init__(self):
        self.__currently_watching_movie: Movie = None
        self.__group_watchlist = WatchList()
        self.__group_name: str = "Group"
        self.__group_members: list = []
        self.__group_comments: list = []
        self.__group_reviews: list = []

    @property
    def currently_watching_movie(self) -> Movie:
        return self.__currently_watching_movie

    @property
    def group_watchlist(self) -> WatchList:
        return self.__group_watchlist

    @property
    def group_name(self) -> str:
        return self.__group_name

    @property
    def group_members(self) -> list:
        return self.__group_members

    @property
    def group_comments(self) -> list:
        return self.__group_comments

    @property
    def group_reviews(self) -> list:
        return self.__group_reviews

    def set_current_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self.__currently_watching_movie = movie

    def change_group_name(self, name: str):
        if len(name) <= 30:
            self.__group_name = name

    def add_member(self, user: User):
        add = True
        for m in self.__group_members:
            if m.user_name == user.user_name:
                add = False

        if add:
            self.__group_members.append(user)

    def remove_member(self, user: User):
        remove_m = None
        for m in self.__group_members:
            if m.user_name == user.user_name:
                remove_m = m

        if remove_m is not None:
            self.__group_members.remove(remove_m)

    def add_group_review(self, user: User, review: Review):
        for m in self.__group_members:
            if m.user_name == user.user_name:
                review_string = str(m) + ": " + str(review.movie) + ", Description: " + str(review.review_text) + ", Rating: " + str(review.rating)
                self.__group_reviews.append(review_string)

    def add_comment(self, user: User, comment: str):
        for m in self.__group_members:
            if m.user_name == user.user_name:
                comment_string = str(m) + ": " + comment
                self.__group_comments.append(comment_string)
