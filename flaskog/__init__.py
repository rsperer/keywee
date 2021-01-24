from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskog import routes


