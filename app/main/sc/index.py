from flask import render_template
from app import app

@app.route('/snapchat')
def load_ig():
    return render_template('sc_index.html')