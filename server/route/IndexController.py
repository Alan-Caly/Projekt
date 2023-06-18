from flask import render_template
from server import app
from server.src.sqlite.Database import Database


class IndexController:
    """ IndexController """
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def render_index(cls):
        """ render_index """
        based = Database()
        QUERRY = 'SELECT car.picture, brand.brand_name, color.color_name, body_type.body_type_name, gear_box.gear_box_name, seats.seat_count, engine_type.engine_type_name FROM car JOIN brand ON car.id_brand = brand.id JOIN color ON car.id_color = color.id JOIN body_type ON car.id_body_type = body_type.id JOIN gear_box ON car.id_gear_box = gear_box.id JOIN seats ON car.id_seats = seats.id JOIN engine_type ON car.id_engine_type = engine_type.id'
        based.execute(QUERRY)
        data = based.fetchall()
        print(data)

        return render_template(f'/page/home_page.html', data = data)


app.add_url_rule('/', view_func=IndexController().render_index)
