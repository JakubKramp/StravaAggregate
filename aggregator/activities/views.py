from flask import Blueprint, jsonify, request
from flask.views import View
from sqlalchemy.exc import IntegrityError

from app import db
from aggregator.models import Activity

activities_blueprint = Blueprint('activities', __name__, url_prefix='/activities')

class ActivityDetailView(View):
    methods = ("GET",)
    def dispatch_request(self, id):
        activity = db.session.execute(db.select(Activity).filter_by(id=id)).scalar_one()
        return jsonify({'distance': activity.distance})


activities_blueprint.add_url_rule('/<int:id>', view_func=ActivityDetailView.as_view('activity_detail'))


@activities_blueprint.route('/create/', methods=('POST',))
def signup():
    activity = Activity(**request.json)
    try:
        db.session.add(activity)
        db.session.commit()
    except IntegrityError:
        return jsonify({'error': 'Username taken'})
    return jsonify({'user': activity.user_id})
