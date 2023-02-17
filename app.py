import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('aggregator/config/settings.py')
db.init_app(app)
migrate = Migrate(app, db)
from aggregator.users.views import users_blueprint
from aggregator.activities.views import activities_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(activities_blueprint)