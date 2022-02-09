from flask import Flask
from flask_restful import Api

from resources.route import init_route
from database.db import init_db

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)

db = init_db(app)
init_route(api)
