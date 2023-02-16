from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from aggregator import db
from aggregator.users.models import User

users_blueprint = Blueprint('users', __name__, url_prefix='/users')


@users_blueprint.route('/signup/', methods=('POST',))
def signup():
    user = User(**request.json)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return jsonify({'error': 'Username taken'})
    return jsonify({'username': user.username})
