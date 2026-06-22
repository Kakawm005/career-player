from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "9cbf5269a37905acb58ea88823c22781"

database = SQLAlchemy(app) 

from modocarreira import routes