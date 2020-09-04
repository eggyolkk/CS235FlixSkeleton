from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User
from domainmodel.watching_simulation import WatchingSimulation

import pytest


@pytest.fixture
def watching_simulation():
    new_watching_simulation = WatchingSimulation()
    new_watching_simulation.add_member(User('Martin', 'pw12345'))
    return new_watching_simulation


@pytest.fixture
def user1():
    return User('Martin', 'pw12345')


@pytest.fixture
def user2():
    return User('Ian', 'pw67890')


@pytest.fixture
def review1():
    review1 = Review(Movie("Moana", 2016), "Great movie", 8)
    return review1


@pytest.fixture
def review2():
    review2 = Review(Movie("Ice Age", 2002), "Bad movie", 2)
    return review2


def test_set_current_movie(watching_simulation):
    watching_simulation.set_current_movie(Movie("Moana", 2016))
    assert str(watching_simulation.currently_watching_movie) == "<Movie Moana, 2016>"


def test_set_current_movie_non_movie_object(watching_simulation):
    watching_simulation.set_current_movie(Movie("Moana", 2016))
    watching_simulation.set_current_movie("Moana")
    assert str(watching_simulation.currently_watching_movie) == "<Movie Moana, 2016>"


def test_change_group_name(watching_simulation):
    assert str(watching_simulation.group_name) == "Group"
    watching_simulation.change_group_name("My Group")
    assert str(watching_simulation.group_name) == "My Group"


def test_change_group_name_invalid_name(watching_simulation):
    watching_simulation.change_group_name("My Group")
    watching_simulation.change_group_name("qwertyuiopasdfghjklzxcvbnmqwertyui")
    assert str(watching_simulation.group_name) == "My Group"


def test_add_member(watching_simulation, user2):
    watching_simulation.add_member(user2)
    assert str(watching_simulation.group_members) == "[<User martin>, <User ian>]"


def test_add_member_twice(watching_simulation, user1, user2):
    watching_simulation.add_member(user2)
    watching_simulation.add_member(user1)
    assert str(watching_simulation.group_members) == "[<User martin>, <User ian>]"


def test_remove_member(watching_simulation, user2):
    watching_simulation.remove_member(user2)
    assert str(watching_simulation.group_members) == "[<User martin>]"


def test_remove_invalid_member(watching_simulation, user2):
    watching_simulation.add_member(user2)
    invalid_user = User('invalid', 'pw0000')
    watching_simulation.remove_member(invalid_user)
    assert str(watching_simulation.group_members) == "[<User martin>, <User ian>]"


def test_add_review_existing_user(watching_simulation, user1, review1, user2, review2):
    watching_simulation.add_member(user2)
    watching_simulation.add_group_review(user1, review1)
    watching_simulation.add_group_review(user2, review2)
    assert str(watching_simulation.group_reviews) == "['<User martin>: <Movie Moana, 2016>, Description: Great movie, Rating: 8', '<User ian>: <Movie Ice Age, 2002>, Description: Bad movie, Rating: 2']"


def test_add_review_non_existing_user(watching_simulation, user1, review1, user2, review2):
    watching_simulation.add_group_review(user2, review2)
    assert str(watching_simulation.group_reviews) == "[]"


def test_add_comment_existing_user(watching_simulation, user2):
    watching_simulation.add_member(user2)
    watching_simulation.add_comment(user2, "Hahahaha")
    watching_simulation.add_comment(user2, "This is funny")
    assert str(watching_simulation.group_comments) == "['<User ian>: Hahahaha', '<User ian>: This is funny']"


def test_add_comment_non_existing_user(watching_simulation, user2):
    watching_simulation.add_comment(user2, "Hahahaha")
    watching_simulation.add_comment(user2, "This is funny")
    assert str(watching_simulation.group_comments) == "[]"
