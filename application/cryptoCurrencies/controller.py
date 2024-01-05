from flask import jsonify, request
from werkzeug import exceptions
from .model import CryptoCurrency
from .. import db


def index():
    cryptoCurrencies = CryptoCurrency.query.all()
    try:
        return jsonify({ "data": [c.json for c in cryptoCurrencies] }), 200
    except:
        raise exceptions.InternalServerError(f"We are working on it")

def show(id):
    print("id", type(id))
    cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()
    try:
        return jsonify({ "data": cryptoCurrency.json }), 200
    except:
        raise exceptions.NotFound(f"You get it")


def create():
    try:
        name, inventor_name, greatest_of_all_time_price, launch_date = request.json.values()

        new_cryptoCurrency = CryptoCurrency(name, inventor_name, greatest_of_all_time_price, launch_date)

        db.session.add(new_cryptoCurrency)
        db.session.commit()

        return jsonify({ "data": new_cryptoCurrency.json }), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request")

def update(id):
    data = request.json
    cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(cryptoCurrency, attribute):
            setattr(cryptoCurrency, attribute, value)

    db.session.commit()
    return jsonify({ "data": cryptoCurrency.json })

def destroy(id):
    cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()
    db.session.delete(cryptoCurrency)
    db.session.commit()
    return "Crypto Currency Deleted", 204