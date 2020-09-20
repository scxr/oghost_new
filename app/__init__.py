from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.config import settings
from flask_jwt_extended import JWTManager

import os
app = Flask(__name__)
app.config.from_object(settings.Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app.main.admin import admin, index, links, login, logs
# home page
from app.main.home import index
# instagram
from app.main.ig import index
from app.main.ig.login import index
# tiktok
from app.main.tt import index
from app.main.tt.login import index
# snapchat
from app.main.sc import index
from app.main.sc.login import index
