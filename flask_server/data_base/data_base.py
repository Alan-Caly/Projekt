import sqlite3

con = sqlite3.connect("data_base.db")
cursor = con.cursor()
con.row_factory = sqlite3.Row

with open("schema/init.schema.sql") as file:
    con.executescript(file.read())

with open("schema/insert_data.sql") as file:
    con.executescript(file.read())

con.commit()
