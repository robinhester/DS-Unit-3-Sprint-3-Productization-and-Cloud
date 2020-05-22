from flask import Blueprint, render_template, request
from web_app.models import User

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    users = User.query.all()
    return render_template('layout.html', title='Home', users=users)


@home_routes.route("/about")
def about():
    return "Input a tweet and return who most likely wrote it`"