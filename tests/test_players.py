import pytest
from flask import Flask

from api import create_app


@pytest.fixture(scope='module')
def client() -> Flask:
    '''Create a Flask test client'''
    app = create_app()
    yield app.test_client()


def test_players(client: Flask) -> None:
    '''Test the players endpoint.'''
    response = client.get('/players')
    assert response.status_code == 200
    assert response.json == {'message': 'Get players'}