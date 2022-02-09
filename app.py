from flask import Flask
from flask_restful import Api

from resources.route import init_route
from database.db import init_db

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://nary:nary12321@practice.rmfv4.mongodb.net/todos_db?retryWrites=true&w=majority'
}

db = init_db(app)
init_route(api)

app.run()