from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

class Phish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String, ForeignKey('site_user.username'))
    platform = db.Column(db.String)
    phised_user = db.Column(db.String)
    phished_pword = db.Column(db.String)
    ip = db.Column(db.String)

    
class Site_User(db.Model):
    __tablename__ = "site_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    accounts = relationship("Phish")
    
