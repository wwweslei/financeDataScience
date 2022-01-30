from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_geek():
        return '<h1>Hello from Flask & Docker</h2>'

    return app