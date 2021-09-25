# IMPORTS
from flask import Flask

# LOCAL IMPORTS


app = Flask(__name__)

app.config["SECRET_KEY"] = "7110d8ae50b23a5d1616bf329bc298105da20fe"




@app.route("/")
def index():
    return("hola")