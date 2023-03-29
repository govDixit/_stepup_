
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['SECRET_KEY'] = "f9c22ad42e75821bd8dbf9d88841af7a2d1825a3"
app.config['MONGO_URI'] = "mongodb+srv://govinddixit989:govind123@cluster0.t8hvy7k.mongodb.net/?retryWrites=true&w=majority"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from app import routes