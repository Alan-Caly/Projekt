from flask import render_template
from server import app


class LoginController:
    """ LoginController """
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def render_login(cls):
        """ render_login """
        return render_template(f'/page/login_page.html')


app.add_url_rule('/login', view_func=LoginController().render_login)
