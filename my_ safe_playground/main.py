import scripts.database.main as database
import scripts.strings.main as strings

import json

print(database.get_data())
# print(strings.loader(database.get_data()[2][1][1]))

class Unit:
    def __init__(self, id, name, l_k):
        self.id = id
        self.name = name
        self.l_k = l_k

    def __repr__(self):
        return str({self.id, self.name, self.l_k})

class Lesson:
    def __init__(self, id, name, parts_id, u_id):
        self.id = id
        self.name = name
        self.parts_id = parts_id
        self.u_id = u_id

    def __repr__(self):
        return str({self.id, self.name, self.parts_id, self.u_id})

class Part:
    def __init__(self, id, path, l_id):
        self.id = id
        self.path = path
        self.l_id = l_id

    def __repr__(self):
        return str({self.id, self.path, self.l_id})
    
# class Item:
#     def __init__(self, id, name, character, p_id):
def main():
    data = database.get_data()

    units = [Unit(*unit_data) for unit_data in data[0]]
    lessons = [Lesson(*lesson_data) for lesson_data in data[1]]
    parts = [Part(*part_data) for part_data in data[2]]

    def filter_lessons(lessons, input_id):
        return [lesson for lesson in lessons if lesson.u_id == input_id]

    print("Select a section:")
    for i, unit in enumerate(units, start=1):
        print(f"{i}. {unit.name}")

    section_id = int(input())
    lessons_in_section = filter_lessons(lessons, section_id)

    print("Select a lesson:")
    for i, lesson in enumerate(lessons_in_section, start=1):
        print(f"{i}. {lesson.name}")

    lesson_id = int(input())
    lesson_parts = json.loads(lessons_in_section[lesson_id - 1].parts_id)

    print (lesson_parts)


main()
