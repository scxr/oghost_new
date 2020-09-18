from app import app
from flask import current_app
@app.route('/admin')
def admin():
    conf = app.config 
    return 'ok'