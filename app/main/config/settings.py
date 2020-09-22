import os
class Config:
    SECRET_KEY = os.urandom(32)
    TIKTOK_DOMAIN = 'tiktokanalytics.net'
    SNAPCHAT_DOMAIN = 'snapchatanalytics.net'
    INSTAGRAM_DOMAIN = 'lnstagramanalytics.net'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    JWT_SECRET_KEY = os.urandom(32)
    JWT_TOKEN_LOCATION = ['cookies', 'headers']
    COMPANY_TO_USE = 'google'