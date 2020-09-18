from flask_sqlalchemy import SQLAlchemy;
from enum import Enum;

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



class Restaurant(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.Integer(), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    web_page = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
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
            # do not serialize the password, its a security breach
        }


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(520), unique=False, nullable=False)
    is_typical = db.Column(db.Boolean(), unique=False, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable = True)
    restaurant = db.relationship("Restaurant", lazy=True)

    def __repr__(self):
        return '<Dish %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "description": self.description,
            "is_typical": self.is_typical,
          
            # do not serialize the password, its a security breach
        }

class FileContents(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120))
    data = db.Column(db.LargeBinary)

class SeedData():

    @staticmethod
    def generate_restaurant_and_dishes():

        dishes= [{
            "description": "Bacon ipsum dolor amet cupim jerky ribeye picanha kevin biltong shoulder pork belly tri-tip.",
            "is_typical": True, 
            "name": "Calamares"
        }, 
        {
            "description": "Bacon ipsum y filet mignon ribeye. Drumstick tenderloin capicola bresaola, strip ste dolor amet pork belly tri-tip.", 
            "is_typical": True, 
            "name": "Tortilla patatas"
        }, 
        {
            "description": "jhasdhdg mejillones en vinagre", 
            "is_typical": False, 
            "name": "albondigas"
        }, 
        {
            "description": "jhasdhdg macarrones en vinagre", 
            "is_typical": False, 
            "name": "macarrones con tomate"
        }, 
        {
            "description": "jhasdhdg alcachofas en tomate",
            "is_typical": True, 
            "name": "alcachofas con jamon"
        }]
        
        restaurant1 = Restaurant(email="hellow@bakk.com",
        name = "Erwing",
        address = "Calle de la amargura",
        phone = 34468090,
        web_page = "www.typett.es",
        is_active = True) 
        db.session.add(restaurant1)
        db.session.commit()

        for dish in dishes:
            dish1 = Dish(name=dish["name"], is_typical=dish["is_typical"], description=dish["description"], restaurant_id= restaurant1.id)
            db.session.add(dish1)
            db.session.commit()

        
      
        

