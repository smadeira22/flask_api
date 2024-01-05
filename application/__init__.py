from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gsltdkng:oUjS-P6qR2Y3Kr3NR4JK-hfHrvLnuS_m@tyke.db.elephantsql.com/gsltdkng"

db = SQLAlchemy(app)

