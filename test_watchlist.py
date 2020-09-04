from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

import pytest


@pytest.fixture
def watchlist():
    new_watchlist = WatchList()
    new_watchlist.add_movie(Movie("Moana", 2016))
    new_watchlist.add_movie(Movie("Ice Age", 2002))
    new_watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    return new_watchlist


def test_add_movie(watchlist):
    assert str(watchlist.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_add_movie_twice(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    assert str(watchlist.watchlist) == "[<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]"
    assert watchlist.size() == 3


def test_add_non_movie(watchlist):
    watchlist.add_movie(None)
    assert str(watchlist.watchlist) == "[<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]"
    assert watchlist.size() == 3


def test_remove_movie(watchlist):
    watchlist.remove_movie(Movie("Ice Age", 2002))
    assert str(watchlist.watchlist) == "[<Movie Moana, 2016>, <Movie Guardians of the Galaxy, 2012>]"
    assert watchlist.size() == 2


def test_remove_movie_not_in_watchlist(watchlist):
    watchlist.remove_movie(Movie("Invalid", 2002))
    assert str(watchlist.watchlist) == "[<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]"
    assert watchlist.size() == 3


def test_remove_non_movie(watchlist):
    watchlist.remove_movie(None)
    assert str(watchlist.watchlist) == "[<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]"
    assert watchlist.size() == 3


def test_select_movie(watchlist):
    assert str(watchlist.select_movie_to_watch(1)) == "<Movie Ice Age, 2002>"


def test_select_movie_with_invalid_index(watchlist):
    assert str(watchlist.select_movie_to_watch(3)) == "None"
    assert str(watchlist.select_movie_to_watch(-1)) == "None"


def test_first_movie(watchlist):
    assert str(watchlist.first_movie_in_watchlist()) == "<Movie Moana, 2016>"


def test_first_movie_empty_watchlist(watchlist):
    new_watchlist = WatchList()
    assert str(new_watchlist.first_movie_in_watchlist()) == "None"


def test_iteration(watchlist):
    check_string = ""
    for movie in watchlist:
        check_string += str(movie)
    assert check_string == "<Movie Moana, 2016><Movie Ice Age, 2002><Movie Guardians of the Galaxy, 2012>"