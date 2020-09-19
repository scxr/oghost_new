from flask import render_template
from app import app

@app.route('/instagram')
def load_ig():
    return render_template('ig_index.html')