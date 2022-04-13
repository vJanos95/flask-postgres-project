from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()

class StatData(db.Model):
    __tablename__= 'data'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10))
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(20), db.ForeignKey('user.name'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    
    
    def __init__(self,license_plate,amount,date, user_id, car_id, user_name):
        self.license_plate = license_plate
        self.amount = amount
        self.date = date
        self.user_id = user_id
        self.car_id = car_id
        self.user_name = user_name

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(30))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    
    def __init__(self,uname,password,name,email, is_admin):
        self.uname = uname
        self.password = password
        self.name = name
        self.email = email
        self.is_admin = is_admin
        
    def __repr__(self):
        return f"{self.id} {self.name} : {self.uname}, {self.password}, {self.email}, {self.is_admin}"

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key = True)
    manufacturer = db.Column(db.String(30))
    model = db.Column(db.String(30))
    year = db.Column(db.Integer)
    license_plate = db.Column(db.String(20), unique = True)
    
    def __init__(self,manufacturer,model, license_plate):
        self.manufacturer = manufacturer
        self.model = model
        self.license_plate = license_plate