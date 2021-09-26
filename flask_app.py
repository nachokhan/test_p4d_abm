# IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# LOCAL IMPORTS
from db_configdata import SQL_CONNECTION_STRING

app = Flask(__name__)

app.config["SECRET_KEY"] = "7110d8ae50b23a5d1616bf329bc298105da20fe"
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_CONNECTION_STRING
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

from views.users import users

app.register_blueprint(users)


@app.route("/")
def index():
    return("hola")
