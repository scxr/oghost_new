from app import db
import random
from app.main.config.models import User, Phish, Site_User
usr = Site_User.query.filter_by(username='xo').first()
print(usr.accounts)
