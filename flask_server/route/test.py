from flask_server import app


@app.route('/')
def test():
    return "Hello world"
