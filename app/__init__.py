from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.config import settings
from flask_jwt_extended import JWTManager

import os
app = Flask(__name__)
app.config.from_object(settings.Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)

from app.main import admin, index, links, login, logs