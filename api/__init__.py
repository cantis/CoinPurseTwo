import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create Global Objects
db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    '''Create and configure the CoinPurse instance of the Flask application.'''

    # Create flask app
    app = Flask(__name__)
    load_configuration(app)

    # from api.models import bad_table, character, player, BaseModel, SoftDeleteBaseModelclc
    from api.models import character # noqa: F401
    db.init_app(app)
    migrate.init_app(app, db)

    # Import Route modules
    from api.routes import characters, home, players

    # Register Blueprints
    app.register_blueprint(home.home_bp)
    app.register_blueprint(characters.character_bp)
    app.register_blueprint(players.player_bp)

    return app


def load_configuration(app: Flask) -> None:
    '''Load configuration from file based on environment.'''

    environment = os.getenv('FLASK_ENV', 'development')
    load_result = False

    match environment:
        case 'production':
            load_result = app.config.from_pyfile('../instance/config.cfg')
        case 'development':
            load_result = app.config.from_pyfile('../instance/config.dev.cfg')
        case 'test':
            load_result = app.config.from_pyfile('../instance/config.test.cfg')

    if load_result is False:
        raise Exception(f'Failed to load configuration file for {environment} environment.')
