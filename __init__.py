from flask import Flask
app = Flask(__name__)
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
app.secret_key = 'Ameypict26'
app.config['JWT_SECRET_KEY'] = '9a6256d8c7678c69c4d82f4a'
from pymongo.mongo_client import MongoClient 
from pymongo.server_api import  ServerApi 
import requests 
jwt = JWTManager(app)
login_manager = LoginManager(app)
login_manager.login_view = 'app_routes.login'
app.config['JWT_ALGORITHM'] = 'HS256'
from .routes import app_routes
app.register_blueprint(app_routes)
csrf = CSRFProtect(app)
from project.database import client  


    
