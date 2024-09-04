import scripts.database.main as database

def get_overall_data():
    units = database.execute("SELECT * FROM units;")
    lessons = database.execute("SELECT * FROM lessons;")
    parts = database.execute("SELECT * FROM parts;")
    items = database.execute("SELECT * FROM items;")

    return units, lessons, parts, items