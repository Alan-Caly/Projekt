from flask_server import app
from flask import render_template

@app.route('/')
def test():
    return render_template('HTML_login.html')
