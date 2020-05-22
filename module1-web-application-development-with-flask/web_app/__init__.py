"""
Function file for creating app using flask
"""

import os

from dotenv import load_dotenv
from flask import Flask
from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.models import db, migrate


DATABASE_URL = os.getenv("DATABASE_URL")
load_dotenv()


def create_app():
    """
    Create and configure the instance of the
    flask app for the routes and database
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URL"] = DATABASE_URL
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    # app.register_blueprint(twitter_routes)
    app.register_blueprint(twitter_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
