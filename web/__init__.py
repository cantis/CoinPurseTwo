from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello_world():
        return '<h1>Hello, World!</h1>'

    return app