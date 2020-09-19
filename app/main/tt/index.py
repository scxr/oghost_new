from flask import render_template
from app import app

@app.route('/tiktok/')
def load_tt():
    return render_template('tiktok/tt_index.html')