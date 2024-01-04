from application import app ## app from __init__.py

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")