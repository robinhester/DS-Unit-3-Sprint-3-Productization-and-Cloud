from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.models import db, migrate


DATABASE_URI = "sqlite:///C:\\Users\\angel\\Desktop\\project\\Sprint_3\\DS-Unit-3-Sprint-3-Productization-and-Cloud\\module1-web-application-development-with-flask\\twitter_data.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
