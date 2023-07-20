from datetime import datetime
from flask import Flask
from os import environ
import pytest

from api import create_app, db
from api.models import player, character

# region Fixtures


@pytest.fixture(scope='session')
def app():
    '''Create a Flask test client'''

    # set environment to testing
    environ['FLASK_ENV'] = 'test'
    app = create_app()

    yield app


@pytest.fixture(scope='function')
def client(app):
    '''Setup the database for testing'''
    # N.B. This is a function-scoped fixture, so it will run once per test function
    with app.app_context():
        client = app.test_client()
        db.create_all()
        # add a player
        new_player = player.Player(
            first_name='Test',
            last_name='Player',
            email='testplay@noplace.com',
            phone='555-555-5555',
            is_active=True,
            is_admin=False,
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_player)
        db.session.commit()

        yield client
        db.drop_all()


# endregion


def test_get_players(client: Flask) -> None:
    # Arrange

    # Act
    result = client.get('/players', follow_redirects=True)

    # Assert
    assert result.status_code == 200
    assert result.json == {'message': 'Get players'}


def test_add_player(client: Flask) -> None:
    '''Test the POST /players endpoint.'''
    # Arrange
    url = '/players'

    # Act
    response = client.post(url)

    # Assert
    assert response.status_code == 200
    assert response.json == {'message': 'Add player'}


def test_players(client: Flask) -> None:
    response = client.get('/players')
    assert response.status_code == 200
    assert response.json == {'message': 'Get players'}


def test_update_player(client: Flask) -> None:
    '''Test the PUT /players/<player_id> endpoint.'''
    # Arrange
    player_id = 1
    url = f'/players/{player_id}'

    # Act
    response = client.put(url)

    # Assert
    assert response.status_code == 200
    assert response.json == {'message': 'Update player'}


def test_delete_player(client: Flask) -> None:
    '''Test the DELETE /players/<player_id> endpoint.'''
    # Arrange
    player_id = 1
    url = f'/players/{player_id}'

    # Act
    response = client.delete(url)

    # Assert
    assert response.status_code == 200
    assert response.json == {'message': 'Delete player'}
