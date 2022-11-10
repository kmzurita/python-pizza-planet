from datetime import datetime

from app.common.constants import (
    MAX_NAME_LENGTH, DNI_LENGTH, MAX_ADDRESS_LENGTH, MAX_PHONE_LENGTH)
from app.plugins import db


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(MAX_NAME_LENGTH))
    client_dni = db.Column(db.String(DNI_LENGTH))
    client_address = db.Column(db.String(MAX_ADDRESS_LENGTH))
    client_phone = db.Column(db.String(MAX_PHONE_LENGTH))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))

    size = db.relationship('Size', backref=db.backref('size'))
    ingredient_detail = db.relationship(
        'IngredientOrderDetail', backref=db.backref('ingredient_order_detail'))
    beverage_detail = db.relationship(
        'BeverageOrderDetail', backref=db.backref('beverage_order_detail'))


class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), nullable=False)
    price = db.Column(db.Float, nullable=False)


class IngredientOrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    ingredient_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    ingredient = db.relationship(
        'Ingredient', backref=db.backref('ingredient'))


class BeverageOrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    beverage_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    beverage = db.relationship(
        'Beverage', backref=db.backref('beverage'))
