from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    d1 = Director(id=1, name="John")
    d2 = Director(id=2, name="Alex")
    d3 = Director(id=3, name="Kevin ")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def director_dao():
    genre_dao = GenreDAO(None)
    comedy = Genre(id=1, name="Comedy")
    drama = Genre(id=2, name="Drama")
    horror = Genre(id=3, name="Horror")

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, drama])
    genre_dao.create = MagicMock(return_value=horror)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao
