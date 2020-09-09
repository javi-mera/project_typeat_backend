from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Enum

db = SQLAlchemy()

class Gender(enum.Enum):
    1: "male",
    2: "female",

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(Integer, unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    male = db.Column(db.Boolean(), unique=False, nullable=False)
    female = db.Column(db.Boolean(), unique=False, nullable=False)
    # Prueba: gender = db.Column(db.Enum(Gender))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

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

assignments = db.Table("assignments",
    db.Column("preferredDishes_id", db.Integer, db.ForeignKey("preferredDishes.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),

)

class Role_type(enum.Enum):
    1: "user",
    2: "restaurant",

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    web_page = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    dishes = db.relationship("Dish", lazy=True)
    #role = db.Column(db.Enum(Role_type)) # Cómo indicar el rol? booleano?integer?

    def __repr__(self):
        return '<Restaurant %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "adress": self.last_name,
            "phone":self.phone,
            "email": self.email,
            "web_page": self.web_page,
            # do not serialize the password, its a security breach
        }


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    is_typical = db.Column(db.Boolean(), unique=False, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable = False)
    restaurant = db.relationship("Restaurant", lazy=True)

      def __repr__(self):
        return '<Dish %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "description": self.last_name,
            "is_typical": self.is_typical,
          
            # do not serialize the password, its a security breach
        }

class PreferredDishes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"), nullable = False)
    dish = db.relationship("Dish", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    user = db.relationship("User", lazy=True)