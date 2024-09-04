import scripts.database.main as database

def types_interpreter():
    class OneItemType:
        def __init__(self, id, name, character):
            self.id = id
            self.name = name
            self.character = character

        def __repr__(self):
            return str({self.id, self.name, self.character})

    database_types = database.execute("SELECT id, name, character FROM types;")
    types = []
    for i in database_types:
        types.append(OneItemType(i[0], i[1], i[2]))
    return types