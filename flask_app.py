# IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# LOCAL IMPORTS
from db_configdata import SQL_CONNECTION_STRING

app = Flask(__name__)

app.config["SECRET_KEY"] = "7110d8ae50b23a5d1616bf329bc298105da20fe"
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_CONNECTION_STRING
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# FLASK USER configuration settings
app.config['USER_ENABLE_EMAIL'] = False
app.config['USER_APP_NAME'] = "Pix4D Drones"


db = SQLAlchemy(app)

from views.home import home
from views.users import users
from views.drones import drones

app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(drones)
