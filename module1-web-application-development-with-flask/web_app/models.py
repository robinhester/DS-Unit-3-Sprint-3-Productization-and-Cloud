"""
SqlAlchemy models for twitoff
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    """
    Twitter users that we pull and analyze tweets for
    """
    id = db.Column(db.BigInteger, primary_key=True)
    twit_handle = db.Column(db.String(15), nullable=False)
    followers_count = db.Column(db.Integer)
    location = db.Column(db.String)
    newest_tweet_id = db.Column(db.BigInteger)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


class Tweet(db.Model):
    """
    tweets taken from our api
    """
    id = db.Column(db.Integer, primary_key=True)
    tweets = db.Column(db.Unicode(300))
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet: {}>'.format(self.tweets)
