import scripts.database.main as database
import scripts.brackets.main as brackets


with open('text.txt', 'r') as f:
    text = f.read()

new = brackets.edit_text_with_brackets(text)
print(new)