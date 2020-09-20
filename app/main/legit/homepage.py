from flask import request, render_template
from app import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, 
    create_refresh_token, get_jwt_identity, set_access_cookies, set_refresh_cookies
)
@app.route('/homepage')
@jwt_required
def homepage():
    current_user = get_jwt_identity()
    return render_template('homepage.html', curr = current_user)
#pprint(insta_scrape('katyperry'))
