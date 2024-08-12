from flask import Flask
from app.core.config import Config
from app.core.db import init_db
from app.api.views.url_view import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)

    app.register_blueprint(bp, url_prefix='/')

    return app