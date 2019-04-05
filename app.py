from flask import Flask, g
from router import create_routes 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECTEY_KEY='dev'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    with app.app_context():
        create_routes()
    return app
