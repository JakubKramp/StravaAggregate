from app import db


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    moving_time = db.Column(db.Integer)
    elapsed_time = db.Column(db.Integer)
    start_time = db.Column(db.DateTime)
    average_speed = db.Column(db.Float)
    max_speed = db.Column(db.Float)
    calories = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

