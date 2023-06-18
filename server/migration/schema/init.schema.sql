DROP TABLE IF EXISTS user_data;
DROP TABLE IF EXISTS car;
DROP TABLE IF EXISTS brand;
DROP TABLE IF EXISTS color;
DROP TABLE IF EXISTS body_type;
DROP TABLE IF EXISTS gear_box;
DROP TABLE IF EXISTS seats;
DROP TABLE IF EXISTS engine_type;

CREATE TABLE user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email TEXT NOT NULL,
    phone_number VARCHAR(9) NOT NULL,
    adress TEXT NOT NULL,
    zip_code VARCHAR(6) NOT NULL,
    city TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE brand (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_name VARCHAR(20) NOT NULL
);

CREATE TABLE color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color_name VARCHAR(20) NOT NULL
);

CREATE TABLE body_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    body_type_name VARCHAR(20) NOT NULL
);

CREATE TABLE gear_box (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gear_box_name VARCHAR(20) NOT NULL
);

CREATE TABLE seats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seat_count INTEGER NOT NULL
);

CREATE TABLE engine_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    engine_type_name VARCHAR(20) NOT NULL
);


CREATE TABLE car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    picture TEXT NOT NULL,
    id_brand INT,
    id_color INT,
    id_body_type INT,
    id_gear_box INT,
    id_seats INT,
    id_engine_type INT,
    FOREIGN KEY(id_brand) REFERENCES brand(id),
    FOREIGN KEY(id_color) REFERENCES color(id),
    FOREIGN KEY(id_body_type) REFERENCES body_type(id),
    FOREIGN KEY(id_gear_box) REFERENCES gear_box(id),
    FOREIGN KEY(id_seats) REFERENCES seats(id),
    FOREIGN KEY(id_engine_type) REFERENCES engine_type(id)
);
