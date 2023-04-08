from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Global Objects
db = SQLAlchemy()

def create_app(test_config=None) -> Flask:
    '''Create and configure an instance of the Flask application.'''
    app = Flask(__name__, instance_relative_config=True)

    # Initialize global objects
    db.init_app(app)


    @app.route('/')
    def hello_world():
        return '<h1>Hello, World!</h1>'

    return app
