from flask import Blueprint


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return f"Twitter Page"

@home_routes.route("/about")
def about():
    return "Input a tweet and return who most likely wrote it`"