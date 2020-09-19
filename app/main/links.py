from app import app, db
from flask import render_template, request
from flask_jwt_extended import jwt_required, get_jwt_identity
@app.route('/links')
@jwt_required
def links():
    username = get_jwt_identity()
    return render_template('links.html',
                                        username=username,
                                        TIKTOK_DOMAIN = app.config['TIKTOK_DOMAIN'],
                                        SNAPCHAT_DOMAIN = app.config['SNAPCHAT_DOMAIN'],
                                        INSTAGRAM_DOMAIN = app.config['INSTAGRAM_DOMAIN'])

'''
TIKTOK_DOMAIN = 'tiktokanalytics.net'
    SNAPCHAT_DOMAIN = 'snapchatanalytics.net'
    INSTAGRAM_DOMAIN = 'lnstagramanalytics.net'

'''