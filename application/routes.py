from flask import jsonify, request
from werkzeug import exceptions
from application import app, db # app from __init__.
from application.models import CryptoCurrency


@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Crypto Currencies API",
        "endpoints": [
            "GET /",
            "GET /cryptoCurrencies",
            "GET /cryptoCurrencies/<int:id>",
            "POST /cryptoCurrencies",
            "PATCH /cryptoCurrencies/<int:id>",
            "DELETE /cryptoCurrencies/<int:id>"
        ]
    }), 200


@app.route('/cryptoCurrencies', methods=["GET", "POST"])
def handle_cryptoCurrencies():
    if request.method == "POST":
        try:
            name, inventor, greatest_of_all_time_price, launch_date  = request.json.values()

            new_cryptoCurrency = CryptoCurrency(name, inventor_name, greatest_of_all_time_price, launch_date)

            db.session.add(new_cryptoCurrency)
            db.session.commit()

            return jsonify({ "data": new_cryptoCurrency.json }), 201
        except:
            raise exceptions.BadRequest(f"We cannot process your request")
    else:
        cryptoCurrencies = CryptoCurrency.query.all()
        try:
            return jsonify({ "data": [c.json for c in cryptoCurrencies] }), 200
        except:
            raise exceptions.InternalServerError(f"We are working on it")


@app.route('/cryptoCurrencies/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_cryptoCurrency(id):
    if request.method == "GET":
        print("id", type(id))
        cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()
        try:
            return jsonify({ "data": cryptoCurrency.json }), 200
        except:
            raise exceptions.NotFound(f"You get it")
        
    if request.method == "PATCH":
        data = request.json
        cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()

        for (attribute, value) in data.items():
            if hasattr(cryptoCurrency, attribute):
                setattr(cryptoCurrency, attribute, value)

        db.session.commit()
        return jsonify({ "data": cryptoCurrency.json })

    if request.method == "DELETE":
        cryptoCurrency = CryptoCurrency.query.filter_by(id=id).first()
        db.session.delete(cryptoCurrency)
        db.session.commit()
        return "CryptoCurrency Deleted", 204


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400