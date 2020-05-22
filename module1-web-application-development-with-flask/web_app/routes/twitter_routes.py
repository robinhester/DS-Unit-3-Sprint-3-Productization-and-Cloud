"""
retrieve tweets, embeddings, and persist in the database
"""

import basilica, os, tweepy

from dotenv import load_dotenv
from flask import Blueprint, render_template
from web_app.models import db, Tweet, User

twitter_routes = Blueprint("twitter_routes", __name__)


load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
TWITTER_AUTH.set_access_token(TWITTER_ACCESS_TOKEN,
                              TWITTER_ACCESS_TOKEN_SECRET)

TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(BASILICA_API_KEY)

@twitter_routes.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    return render_template('layout.html', title='DB RESET!', users=[])


@twitter_routes.route("/users/<twit_handle>")
def get_user(screen_name=None):
    handle = TWITTER.get_user(screen_name)
    tweet_info = TWITTER.user_timeline(screen_name, tweet_mode='extended', count=150)
    
    db_user = User(id=TWITTER.id)
    db_user.twit_handle = TWITTER.screen_name
    db_user.followers_count = TWITTER.followers_count
    db_user.location = TWITTER.location
    db_user.newest_tweet_id = TWITTER.tweets[0].id

    db.session.add(db_user)
    db.session.commit()

    return jsonify({
        "user:": handle.__json,
        "tweets": [tweet_info.full_text for tweet in tweet_info]
    })


