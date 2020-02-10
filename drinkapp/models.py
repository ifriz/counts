from datetime import datetime
from sqlalchemy import func, desc

from drinkapp import db

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def get_count(channel_name):
        return Drink.query.filter(Drink.channel == channel_name).count()

    @staticmethod
    def get_drink(name):
        return Drink.query.filter(Drink.channel == name)

    @staticmethod
    def top(num):
        return db.session.query(Drink.channel, func.count(Drink.channel).label('counts')).\
            group_by(Drink.channel).order_by(desc(func.count(Drink.channel))).limit(num)

    def __repr__(self):
        return "Drink '{}': '{}'>".format(self.name, self.channel)

    @property
    def serialize(self):
        return {
            'channel': self.channel,
            'data': self.date,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(50), nullable=False)
    drinkcounts = db.relationship('Drink', backref='user', lazy='dynamic')

    @staticmethod
    def get_user_by_name(name):
        return User.query.filter_by(username=name).first()

    def __repr__(self):
        return '<User %r' % self.username
