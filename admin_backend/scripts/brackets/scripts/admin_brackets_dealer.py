import admin_backend.scripts.database.main as database

def edit_text_with_brackets(string):

    new_text = string

    class OneItem:
        def __init__(self, name, type):
            self.name = name
            self.type = type

        def __repr__(self):
            return str({self.name, self.type})

    types = database.types()

    output =[]
    for one_type in types:
        #result = []
        found = False
        start = 0
        for i in range(len(string)):
            if string[i] == one_type.character and not found:
                found = True
                start = i+1
                continue
            elif string[i] == one_type.character and found:
                found = False
                new_text = new_text.replace(string[start-1:i+1], '{' + str(one_type.id) + ',' + string[start:i] +'}')
                output.append(OneItem(string[start:i], one_type.id))
            elif found:
                continue
            else:
                continue
    return new_text