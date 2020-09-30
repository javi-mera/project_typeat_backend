#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""

import os
from flask import Flask, request, jsonify, url_for, make_response   
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Dish, Restaurant, Gender, Role, SeedData, FileContents
from flask import request
from flask_sqlalchemy import SQLAlchemy


#login
from werkzeug.security import generate_password_hash, check_password_hash
import uuid 
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.url_map.strict_slashes = False
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

#creando carpeta descargas - borrar
app.config['UPLOAD_FOLDER'] = '/workspace/project_typeat_backend/src/Archivos PDF'

#PROBANDO CORS - borrar   
app.config['CORS_HEADERS'] = 'Content-Type'


# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    SeedData.generate_restaurant_and_dishes()
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
    gender=Gender[request_user["gender"]].value,
    role = Role[request_user["role"]].value)
    db.session.add(user1)
    db.session.commit()

    return jsonify(user1.serialize()), 200

# Modificar o traer un user (¿¿Cómo modificar pwd??)
@app.route('/user/<int:user_id>', methods=['PUT', 'GET'])
def get_single_user(user_id):
    body = request.get_json() #{ 'username': 'new_username'} 
    if request.method == 'PUT':
        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        if "name" in body:
            user1.name = body["name"]
        if "email" in body:
            user1.email = body["email"]
        if "phone" in body:
            user1.phone = body["phone"] 
        if "last_name" in body:
            user1.last_name = body["last_name"]
        if "gender" in body:
            user1.gender = body["gender"]
        db.session.commit()
    if request.method == 'GET':
        user1 = User.query.get(user_id)

    return jsonify(user1.serialize()), 200 

#Eliminar un user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_single_user(user_id):
    user1 = User.query.get(user_id)
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

    return jsonify(dish1.serialize()), 200

#probando a cargar archivos
@app.route('/upload', methods=['GET','PUT'])
def upload():
    if request.method=="PUT":
        file = request.files["fileinput"]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename ))
        print("algop")
        
        return redirect(request.url)

  
# Modificar o traer un dish
@app.route('/dish/<int:dish_id>', methods=['PUT', 'GET'])
def get_single_dish(dish_id):
    body = request.get_json()
    if request.method == 'PUT':
        dish1 = Dish.query.get(dish_id)
        if dish1 is None:
            raise APIException('Dish not found', status_code=404)
        if "name" in body:
            dish.name = body["name"]
        if "description" in body:
            dish.description = body["description"]
        db.session.commit()
    if request.method == 'GET':
        dish1 = Dish.query.get(dish_id)

    return jsonify(dish1.serialize()), 200 

#Eliminar un dish
@app.route('/dish/<int:dish_id>', methods=['DELETE'])
def delete_single_dish(dish_id):
    dish1 = Dish.query.get(dish_id)
    if dish1 is None:
        raise APIException('Dish not found', status_code=404)
    db.session.delete(dish1)
    db.session.commit()    

    return jsonify(dish1.serialize()), 200  


# RESTAURANT

# get all restaurant
@app.route('/restaurant', methods=['GET'])
def get_restaurant():

    restaurant = Restaurant.query.all()
    all_restaurants = list(map(lambda x: x.serialize(), restaurant))

    return jsonify(all_restaurants), 200

# create restaurant
@app.route('/restaurant', methods=['POST'])
def create_restaurant():
    request_restaurant = request.get_json()
    restaurant1 = Restaurant(email=request_restaurant["email"], 
    password=request_restaurant["password"], 
    name=request_restaurant["name"],
    address=request_restaurant["address"], 
    phone=request_restaurant["phone"],
    web_page=request_restaurant["web_page"]  )
    db.session.add(restaurant1)
    db.session.commit()

    return jsonify(restaurant1.serialize()), 200

# Modificar o traer un restaurant
@app.route('/restaurant/<int:restaurant_id>', methods=['PUT', 'GET'])
def get_single_restaurant(restaurant_id):
    body = request.get_json() #{ 'name': 'new_name'}
    if request.method == 'PUT':
        restaurant1 = Restaurant.query.get(restaurant_id)
        if restaurant1 is None:
            raise APIException('Restaurant not found', status_code=404)
        if "name" in body:
            restaurant1.name = body["name"]
        if "email" in body:
            restaurant1.email = body["email"]
        if "address" in body:
            restaurant1.address = body["address"]
        if "phone" in body:
            restaurant1.phone = body["phone"]
        if "web_page" in body:
            restaurant1.web_page = body["web_page"]
        db.session.commit()
    if request.method == 'GET':
        restaurant1 = Restaurant.query.get(restaurant_id)

    return jsonify(restaurant1.serialize()), 200 

#Eliminar un restaurant
@app.route('/restaurant/<int:restaurant_id>', methods=['DELETE'])
def delete_single_restaurant(restaurant_id):
    restaurant1 = User.query.get(restaurant_id)
    if restaurant1 is None:
        raise APIException('Restaurant not found', status_code=404)
    db.session.delete(restaurant1)
    db.session.commit()    

    return jsonify(restaurant1.serialize()), 200    


@app.route('/search', methods=['GET', 'POST'])
def search_results():
    args2=request.args.to_dict(flat=False)
    print(args2['lugar'])
    lugar =''
    plato =''
   
    if args2['lugar'] == [''] and args2['plato'] == ['']:
        return jsonify({'msg':'Añade info'}), 400

    if args2['lugar'] != ['']:
        lugar = args2['lugar'][0].lower()
    else:
        return jsonify({'msg':'Error'}), 301
        #lugar = "vacío"

    if args2['plato'] != ['undefined']:
        plato = args2['plato'][0].lower()
    else:
        plato = args2['plato']
    #print(lugar,1)
    #print(plato,2)
    
   

    return "Not query string", 200  


# 1. Sin datos -> Entregar un 400 e indicar que se requiere al el campo ciudad para procesar.
    # 2. Solo con ciudad -> Todos los restaurantes encontrados en la ciudad.
    # dish_query = Dish.query.filter_by(name='Joe')
    # Los Dish que van se encuentran en los restaurantes de esa ciudad.
    # - Encontrar la ciudad : City.query.filter_by(name='Madrid')
    # - Dish.query.filter_by(restaurant_id: city.restaurants)
    # 3. Ciudad y plato típico -> Los restaurantes según segun la ciudad y el tipo de típico.
    # - Encontrar la ciudad : City.query.filter_by(name='Madrid')
    # - Dish.query.filter_by(restaurant_id: city.restaurants). where(name='<dish_name>')
    # Dish.query.filter(Dish.restaurant_id.in_([123,456])).filter(name ...)

#Arreglar este endpoint para renderizar platos según elementos filtrados
@app.route('/render_results', methods=['GET'])
def render_results():
    args = request.args
    args2=args.to_dict(flat=False)
    #print(args2)
    lugar = args2['lugar'][0].lower()
    plato = args2['plato'][0].lower()
    dishes = Dish.query.all()
    all_dishes = list(map(lambda x: x.serialize(), dishes))
    matchPlatos = list(filter(lambda x: x['name'].lower()==plato, all_dishes))
    #print(matchPlatos)

    return jsonify({"results": matchPlatos}), 200  



def token_required(f):  
    @wraps(f)  
    def decorator(*args, **kwargs):

        token = None 

        if 'x-access-tokens' in request.headers:  
            token = request.headers['x-access-tokens'] 


        if not token:  
            return jsonify({'message': 'a valid token is missing'})   


        try:  
            data = jwt.decode(token, app.config["SECRET_KEY"]) 
            current_user = Users.query.filter_by(id=data['id']).first()  
        except:  
            return jsonify({'message': 'token is invalid'})
        
        return f(current_user, *args, **kwargs)

    return decorator 


@app.route('/register', methods=['GET', 'POST'])
def signup_user():  
 data = request.get_json()  

 hashed_password = generate_password_hash(data['password'], method='sha256')
 
 new_user = User(name=data['name'], last_name=data['last_name'], phone=data['phone'], email=data['email'], gender = Gender[data['gender']].value, password=hashed_password, role = Role[data['role']].value) 
 db.session.add(new_user)  
 db.session.commit()    

 return jsonify({'message': 'registered successfully'})   


@app.route('/login', methods=['GET', 'POST'])  
def login_user(): 
 
    auth = request.authorization  
    print(auth)
     
    if not auth or not auth.username or not auth.password:  
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

    user = User.query.filter_by(email=auth.username).first()   
   
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])  
        return jsonify({'token' : token.decode('UTF-8')}) 
        print(token)    
    return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})