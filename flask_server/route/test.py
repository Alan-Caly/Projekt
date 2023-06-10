from flask_server import app
from flask import render_template

@app.route('/')
def test():
    return render_template('HTML_main.html')

@app.route('/login')
def login():
    return render_template('HTML_login.html')

@app.route('/register')
def register():
    return render_template('HTML_register.html')