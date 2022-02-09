from flask import Flask
from flask_restful import Api
from .database.db import init_db

app = Flask(__name__)
api = Api(app)

db = init_db(app)