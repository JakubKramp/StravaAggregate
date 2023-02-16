import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile('./config/settings.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    from aggregator.users.views import users_blueprint

    app.register_blueprint(users_blueprint)
    return app
