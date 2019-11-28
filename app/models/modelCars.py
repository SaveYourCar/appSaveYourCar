from datetime import datetime
from app import db, login_manager

class CarData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carDataName = db.Column(db.String(100), nullable=False)
    dataType = db.Column(db.Boolean(), nullable=False)
    carDataValues = db.relationship('CarDataValue', backref='category', lazy=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fuel = db.Column(db.String(100), nullable=False)
    matriculation = db.Column(db.DateTime, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    carDataValues = db.relationship('CarDataValue', backref='car_author', lazy=True)
    
class CarDataValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valueInt = db.Column(db.Integer, nullable=True)
    valueDate = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    id_CarData = db.Column(db.Integer, db.ForeignKey('car_data.id'), nullable=False)
    id_Car = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
 