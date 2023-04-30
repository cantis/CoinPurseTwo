import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Global Objects
db = SQLAlchemy()


def create_app(test_config=None) -> Flask:
    '''Create and configure the CoinPurse instance of the Flask application.'''

    # Create flask app
    app = Flask(__name__, instance_relative_config=True)

    load_configuration(app)

    # Initialize global objects
    db.init_app(app)

    # Import Route modules
    from api.routes import home

    # Register Blueprints
    app.register_blueprint(home.home_bp)

    return app


def load_configuration(app: Flask) -> None:
    '''Load configuration from file based on environment.'''

    environment = os.getenv('FLASK_ENV', 'test')

    # Load Configuration
    if environment == 'production':
        if app.config.from_pyfile('config.cfg') is False:
            raise Exception('Failed to load production config.cfg')

    if environment == 'development':
        if app.config.from_pyfile('config.dev.cfg') is False:
            raise Exception('Failed to load development config.dev.toml')

    if environment == 'test':
        if app.config.from_pyfile('config.test.cfg') is False:
            raise Exception('Failed to load test config.test.toml')
