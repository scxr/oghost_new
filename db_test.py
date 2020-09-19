from app import db
import random
from app.main.config.models import User, Phish
usr = User(username='nemo', password='hello')
db.session.add(usr)
db.session.commit()