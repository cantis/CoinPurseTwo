from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        # return render_template('template/home.html')

    return app