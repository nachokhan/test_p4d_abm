from flask import Blueprint
from flask import render_template

# Local imports
# from flask_app import db, app


home = Blueprint(
    "home",
    __name__,
    template_folder="../templates/home",
    static_folder="static",
    static_url_path="/home",
)


@home.route("/", methods=["GET", "POST"])
def init():
    return render_template("home.html")
