from flask import Blueprint
from flask import render_template
from flask_login import login_required
from flask_user import roles_required

# Local imports
# from flask_app import db, app


drones = Blueprint(
    "drones",
    __name__,
    template_folder="../templates/drones",
    static_folder="static",
    static_url_path="/drones",
)


@drones.route("/drones", methods=["GET", "POST"])
@roles_required(["Admin", "Support", "Common"])
def list_drones():
    return render_template("list.html")


@drones.route("/drones/add", methods=["GET", "POST"])
@roles_required(["Admin", "Support"])
def add_drone():
    return render_template("list.html")
