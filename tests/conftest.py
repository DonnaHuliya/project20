from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    d1 = Director(id=1, name="John")
    d2 = Director(id=2, name="Alex")
    d3 = Director(id=3, name="Kevin ")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao
