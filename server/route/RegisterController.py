from flask import render_template
from server import app


class RegisterController:
    """ RegisterController """
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def render_register(cls):
        """ render_register """
        return render_template(f'/page/register_page.html')


app.add_url_rule('/register', view_func=RegisterController().render_register)
