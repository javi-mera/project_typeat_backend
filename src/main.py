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
    user1 = User(email=request_user["email"], 
    password=request_user["password"], 
    name=request_user["name"],
    last_name=request_user["last_name"], 
    phone=request_user["phone"],
    gender=request_user["gender"]  )
    db.session.add(user1)
    db.session.commit()

    return jsonify("Usuario: "+ user1.email+", creado"), 200

# Modificar o traer un user
@app.route('/user/<int:user_id>', methods=['PUT', 'GET'])
def get_single_user(user_id):
    body = request.get_json() #{ 'username': 'new_username'}
    if request.method == 'PUT':
        user1 = User.query.get(person_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        if "username" in body:
            user1.username = body["username"]
        if "email" in body:
            user1.email = body["email"]
        db.session.commit()
    if request.method == 'GET':
        user1 = User.query.get(person_id)
    return jsonify(user1.serialize()), 200 


#Eliminar un user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_single_user(user_id):

    user1 = User.query.get(person_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()    
        
    return jsonify(user1.serialize()), 200    

# DISHES

#get all dishes
@app.route('/dish', methods=['GET'])
def get_dishes():

    dishes = Dish.query.all()
    all_dishes = list(map(lambda x: x.serialize(), dishes))

    return jsonify(all_dishes), 200

#create dish
@app.route('/dish', methods=['POST'])
def create_users():
    request_dish = request.get_json()
    dish1 = Dish(name=request_dish["name"], description=request_dish["description"], is_typical=request_dish["is_typical"])
    db.session.add(dish1)
    db.session.commit()

    return jsonify("Plato: "+ dish1.name+", creado"), 200

# Modificar o traer un dish
@app.route('/dish/<int:dish_id>', methods=['PUT', 'GET'])
def get_single_dish(dish_id):
    body = request.get_json()
    if request.method == 'PUT':
        dish1 = Dish.query.get(dish_id)
        if dish1 is None:
            raise APIException('Dish not found', status_code=404)
        if "name" in body:
            user1.name = body["name"]
        if "description" in body:
            user1.description = body["description"]
        db.session.commit()
    if request.method == 'GET':
        dish1 = Dish.query.get(dish_id)
    return jsonify(user1.serialize()), 200 


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
