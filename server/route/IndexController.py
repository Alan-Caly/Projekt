from flask import render_template
from server import app


class IndexController:
    """ IndexController """
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def render_index(cls):
        """ render_index """
        return render_template(f'/page/home_page.html')


app.add_url_rule('/', view_func=IndexController().render_index)
