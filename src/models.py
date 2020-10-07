#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy;
from enum import Enum;
import json

db = SQLAlchemy()

class Gender(Enum):
  male = 1
  female = 2
  other = 3

class Role(Enum):#cómo funciona?
  foodie = 1
  manager = 2

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role= db.Column(db.Integer(), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.Integer(), unique=False, nullable=False)#hace falta poner nº de caracteres?
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)#preguntar si puede dejarse como nullable True, ya que al crear usuario no se solicita el dato.
    
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "last_name": self.last_name,
            "phone":self.phone,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

preferredDishes = db.Table("preferredDishes",
    db.Column("dish_id", db.Integer, db.ForeignKey("dish.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),

)

class City(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    #latitude = db.Column(db.String(120), unique=True, nullable=False)
    #longitude = db.Column(db.String(120), unique=True, nullable=False)
    restaurants = db.relationship("Restaurant", lazy=True)

    def __repr__(self):
        return '<City %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name
        
        }
    

class Restaurant(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    web_page = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    latitude = db.Column(db.String(120), unique=True, nullable=False)
    longitude = db.Column(db.String(120), unique=True, nullable=False)
    #city = db.Column(db.String(120), unique=True, nullable=False)
    #country = db.Column(db.String(120), unique=True, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable = True)
    cities = db.relationship("City", lazy=True)
    dishes = db.relationship("Dish", lazy=True)
 
    

    def __repr__(self):
        return '<Restaurant %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "address": self.address,
            "phone":self.phone,
            "email": self.email,
            "web_page": self.web_page,
            "city_id": self.city_id,
            "latitude":self.latitude,
            "longitude": self.longitude
            # do not serialize the password, its a security breach
        }


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(520), unique=False, nullable=False)
    is_typical = db.Column(db.Boolean(), unique=False, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable = True)
    restaurant = db.relationship("Restaurant", lazy=True)
    img = db.Column(db.String(520), unique=False, nullable=False)

    def __repr__(self):
        return '<Dish %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "description": self.description,
            "is_typical": self.is_typical,
            "restaurant_id": self.restaurant_id,
            "img": self.img
          
            # do not serialize the password, its a security breach
        }

class FileContents(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120))
    data = db.Column(db.LargeBinary)

class SeedData():

    @staticmethod
    def generate_restaurant_and_dishes():

        #with open("./Data/cities.json") as f:
         #   data = json.load(f)
          #  print(data)


        dishes= [{
            "description": "Bacon ipsum dolor amet cupim jerky ribeye picanha kevin biltong shoulder pork belly tri-tip.",
            "is_typical": True, 
            "name": "Calamares",
            
        }, 
        {
            "description": "Bacon ipsum y filet mignon ribeye. Drumstick tenderloin capicola bresaola, strip ste dolor amet pork belly tri-tip.", 
            "is_typical": True, 
            "name": "Tortilla de patatas",
       
        }, 
        {
            "description": "jhasdhdg mejillones en vinagre", 
            "is_typical": False, 
            "name": "albondigas",
            
        }, 
        
        {
            "description": "jhasdhdg cacachofas en tomate",
            "is_typical": True, 
            "name": "alcachofas",
            
        },
        {
            "description": "jhasdhdg cacachofas en tomate",
            "is_typical": True, 
            "name": "callos",
            
        }
        ]
        
        restaurant1 = Restaurant(
        name = "Cacares",
        address = "Calle de la alegria",
        phone = 344255557,
        email = "caca@mail.com",
        web_page = "www.caca.es",
        is_active = True,
        latitude= "330487",
        longitude ="0068346"
        ) 
        db.session.add(restaurant1)
        db.session.commit()

        for dish in dishes:
            dish1 = Dish(name=dish["name"], is_typical=dish["is_typical"], description=dish["description"], restaurant_id= restaurant1.id)
            db.session.add(dish1)
            db.session.commit() 

class SearchDishSearch:
  def search(self,city,plate):
    results = []
    #print(city)
    #print(plate)
    if city is not None and plate is not None:
      results = self.search_by_city_and_plate(city,plate)

    elif city is not None:
      #print(city, "aquí")  
      results = self.search_by_city(city)
      
    return results

  def search_by_city(self,city):
    cities = City.query.filter_by(name=city).first()
    restaurant_ids = db.session.query(Restaurant.id).filter(Restaurant.city_id == cities.id).all()
    ids = []
    for item in restaurant_ids:
        ids.append(item[0]) 
    results = Dish.query.filter(Dish.restaurant_id.in_(ids)).all()
    results_r = list(map(lambda x: x.serialize(), results))
    #print(results_r)
    return results_r

  def search_by_city_and_plate(self,city,plate):
    #print(plate)
    cities = City.query.filter_by(name=city).first()
    restaurant_ids = db.session.query(Restaurant.id).filter(Restaurant.city_id == cities.id).all()
    ids = []
    for item in restaurant_ids:
        ids.append(item[0]) 
    results = Dish.query.filter(Dish.restaurant_id.in_(ids)).all()
    city_dishes=[]
    for dish in results:
        #print(dish.name)
        #print(plate)
        if(dish.name.lower() == plate.lower()):
            city_dishes.append(dish)
    city_dishes_m = list(map(lambda x: x.serialize(), city_dishes))
    print(city_dishes_m)
    return city_dishes_m

