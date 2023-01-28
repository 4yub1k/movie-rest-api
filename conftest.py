# import pytest

from pytest_factoryboy import register
from tests.factories import MovieFactory, CommentFactory

# Fixture will be api_factory
# Don't forget to register the factory, fixture not found error
register(MovieFactory)
register(CommentFactory)

# @pytest.fixture
# def movie(db, movie_factory):
#     movie = movie_factory.create()
#     return movie
