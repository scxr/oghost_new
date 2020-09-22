from app import app, db
from json import dumps
from flask import request, render_template, redirect, make_response, url_for, session
from app.main.config.models import User
import bcrypt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, 
    create_refresh_token, get_jwt_identity, set_access_cookies, set_refresh_cookies
)

@app.route('/logout')
def signout():
    session['curr'] = ''
    return redirect('/new_user')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/', methods=['GET'])
def landing_page():
    if "curr" in session and session["curr"] != '':
        return redirect(url_for('homepage'))
    return render_template('landing.html')

@app.route('/new_user', methods=['GET', 'POST'])
def create_new():
    if request.method == 'GET':
        

        if request.args:
            error = request.args.get("error")
        else:
            error = None
        return render_template('login_signup.html', error=error)
    if request.method == 'POST':
        data = request.form.to_dict()

        if len(data) == 3:
            if data['code'] == app.config['COMPANY_TO_USE']:
                pass
            else:
                return render_template('login_signup.html', error="Wrong company code")
            username = User.query.filter_by(username=data["username"]).first()
            if username:
                return redirect(url_for("create_new", error="username taken"))
            new_user = User(username=data["username"], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(request.url)
        elif len(data) == 2:
            print(data["username"])
            user = User.query.filter_by(username=data["username"]).first()
            if user is None:
                return redirect(url_for("create_new", error="invalid user"))
            print(str(user.password))
            print(type(data["password"]))
            if user and user.password == data["password"]:
                session["curr"] = data["username"]
                access_token = create_access_token(identity=data["username"])
                refresh_token = create_refresh_token(identity=data["username"])
                if user.is_superuser:
                    resp = make_response(redirect('/dashboard'))
                else:
                    resp = make_response(redirect('/homepage'))
                set_access_cookies(resp, access_token)
                set_refresh_cookies(resp, access_token)
                return resp
            else:
                return redirect(url_for("create_new", error="invalid login supplied"))
        return f'{data}'