from flask import render_template
from server import app


class ContactController:
    """ ContactController """

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def render_contact(cls):
        """ render_contact"""
        return render_template(f'/page/contact_page.html')


app.add_url_rule('/contact', view_func=ContactController().render_contact)
