from app import app, db
from flask import request, render_template, jsonify, make_response, redirect, url_for


@app.route('/')
def homepage():
    return render_template('homepage.html')

