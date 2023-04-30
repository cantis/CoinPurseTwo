import pytest
from flask import Flask

from api import create_app


@pytest.fixture(scope='module')
def client() -> Flask:
    '''Create a test client for the Flask application.'''



    app = create_app()
    yield app.test_client()


def test_home(client):
    '''Test the home endpoint.'''
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to CoinPurse!'}