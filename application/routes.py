from flask import jsonify, request
from werkzeug import exceptions
from application import app, db # app from __init__.



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
