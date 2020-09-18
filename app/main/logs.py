from app import app, db
from flask import request, render_template, jsonify, make_response, redirect, url_for
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, 
    create_refresh_token, get_jwt_identity, set_access_cookies, set_refresh_cookies
)
from app.main.config.models import User, Phish

@app.route('/logs')
@jwt_required
def logs():
    current_user = get_jwt_identity()
    phished_users = Phish.query.all()
    return render_template('logs.html', users=phished_users, username=current_user)