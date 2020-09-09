"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Dish, Restaurant


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# USERS

#get all users
@app.route('/user', methods=['GET'])
def get_users():

    users = User.query.all()
    all_people = list(map(lambda x: x.serialize(), users))

    return jsonify(all_people), 200

#create user
@app.route('/user', methods=['POST'])
def create_user():
    request_user = request.get_json()
    user1 = User(email=request_user["email"], password=request_user["password"], name=request_user["name"] )
    db.session.add(user1)
    db.session.commit()

    return jsonify("Usuario: "+ user1.email+", creado"), 200

# DISHES

#get all dishes
@app.route('/dish', methods=['GET'])
def get_dishes():

    dishes = Dish.query.all()
    all_dishes = list(map(lambda x: x.serialize(), dishes))

    return jsonify(all_dishes), 200

#create user
@app.route('/dish', methods=['POST'])
def create_users():
    request_dish = request.get_json()
    dish1 = Dish(name=request_dish["name"], description=request_dish["description"])
    db.session.add(dish1)
    db.session.commit()

    return jsonify("Usuario: "+ user1.email+", creado"), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
