INSERT INTO user_data (first_name, last_name, email, phone_number, adress, zip_code, city, password)
VALUES ('Ceglan', 'Obly', 'ceglanonly@gmail.com', '111222333', 'Kowalestencyjna 23', '43-203', 'Wroclaw', 'Ostenstacyjne' );

INSERT INTO user_data (first_name, last_name, email, phone_number, adress, zip_code, city, password)
VALUES ('Polip', 'Fialkowski', 'polipfialkowski@gmail.com', '444555666', 'Kowalestencyjna 21', '43-432', 'Wroclaw', 'fialki2' );

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO brand (brand_name)
VALUES ('Volkswagen');

INSERT INTO brand (brand_name)
VALUES ('Honda');

INSERT INTO brand (brand_name)
VALUES ('Audi');

INSERT INTO brand (brand_name)
VALUES ('Mercedes');

INSERT INTO brand (brand_name)
VALUES ('Renault');

INSERT INTO brand (brand_name)
VALUES ('Hyundai');

INSERT INTO brand (brand_name)
VALUES ('Citroen');

INSERT INTO brand (brand_name)
VALUES ('Toyota');

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO color (color_name) VALUES ('red');
INSERT INTO color (color_name) VALUES ('green');
INSERT INTO color (color_name) VALUES ('blue');
INSERT INTO color (color_name) VALUES ('yellow');
INSERT INTO color (color_name) VALUES ('orange');
INSERT INTO color (color_name) VALUES ('purple');
INSERT INTO color (color_name) VALUES ('pink');
INSERT INTO color (color_name) VALUES ('black');
INSERT INTO color (color_name) VALUES ('white');
INSERT INTO color (color_name) VALUES ('gray');
INSERT INTO color (color_name) VALUES ('brown');
INSERT INTO color (color_name) VALUES ('silver');
INSERT INTO color (color_name) VALUES ('gold');
INSERT INTO color (color_name) VALUES ('teal');
INSERT INTO color (color_name) VALUES ('navy');
INSERT INTO color (color_name) VALUES ('magenta');
INSERT INTO color (color_name) VALUES ('lime');
INSERT INTO color (color_name) VALUES ('cyan');

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO body_type (body_type_name) VALUES ('Hatchback');
INSERT INTO body_type (body_type_name) VALUES ('Estate');
INSERT INTO body_type (body_type_name) VALUES ('SUV');
INSERT INTO body_type (body_type_name) VALUES ('Sedan');
INSERT INTO body_type (body_type_name) VALUES ('Coupe');
INSERT INTO body_type (body_type_name) VALUES ('Convertible');
INSERT INTO body_type (body_type_name) VALUES ('Pickup');

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO gear_box (gear_box_name) VALUES ('Automatic');
INSERT INTO gear_box (gear_box_name) VALUES ('Manual');

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO seats (seat_count) VALUES (2);
INSERT INTO seats (seat_count) VALUES (5);

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO engine_type (engine_type_name) VALUES ('DSL(Diesel)');
INSERT INTO engine_type (engine_type_name) VALUES ('ESS(Petrol)');
INSERT INTO engine_type (engine_type_name) VALUES ('HEV(Hybrid)');
INSERT INTO engine_type (engine_type_name) VALUES ('BEV(Electric)');

--|||||||||||||||||||||||||||||||||||||||

INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Audi A7', 3, 12, 4, 1, 2, 4);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Audi Q3', 3, 5, 3, 1, 2, 3);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Citroen C4 X', 7, 9, 4, 1, 2, 4);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Corolla TS', 8, 11, 2, 2, 2, 1);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Honda Civic XI', 2, 1, 4, 2, 2, 2);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Honda CR-v', 2, 1, 3, 2, 2, 2);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Hyundai i30 N', 6, 18, 1, 2, 2, 1);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Mercedes AMG E63', 4, 9, 3, 1, 2, 2);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Renault Austral', 5, 15, 3, 1, 2, 1);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Toyota GR Supra', 8, 4, 6, 2, 1, 2);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Volkswagen Golf VII', 1, 10, 1, 2, 1, 1);
INSERT INTO car (picture, id_brand, id_color, id_body_type, id_gear_box, id_seats, id_engine_type)
VALUES ('Volkswagen T-Cross', 1, 5, 3, 1, 2, 2);