import os
class Config:
    SECRET_KEY = b'\x99\nd\x8c\xa7>sE<CZ\x95r\xb2\xa4\xa5\xd8o\xf0\x85\xf4\xd1r\xd1'
    TIKTOK_DOMAIN = 'tiktokanalytics.net'
    SNAPCHAT_DOMAIN = 'snapchatanalytics.net'
    INSTAGRAM_DOMAIN = 'lnstagramanalytics.net'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    JWT_SECRET_KEY = b'\x99\nd\x8c\xa7>sE<CZ\x95r\xb2\xa4\xa5\xd8o\xf0\x85\xf4\xd1r\xd1'
    JWT_TOKEN_LOCATION = ['cookies', 'headers']
    COMPANY_TO_USE = 'google'