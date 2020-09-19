from flask import render_template
from app import app

@app.route('/snapchat/')
def load_sc():
    return render_template('sc_index.html')