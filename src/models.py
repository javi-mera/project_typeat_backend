from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.Integer(), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)#preguntar si puede dejarse como nullable True, ya que al crear usuario no se solicita el dato.

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

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable = True)
    restaurant = db.relationship("Restaurant", lazy=True)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    web_page = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    dishes = db.relationship("Dish", lazy=True)
    role = db.relationship("Role", lazy=True)

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

