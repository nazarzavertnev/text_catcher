import scripts.database.main as database
import scripts.brackets.main as brackets
import json
#from scripts.brackets.main import *


with open('text.txt', 'r') as f:
    text = f.read()

#new = brackets.Term('new', 2)
#new = database.types()
#print(new[0].character)
print(brackets.find_brackets(text))


#stringq = input()
#print("\033[41m" + str(find_brackets(stringq, rows)) + "\033[0m")
