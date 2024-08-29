import admin_backend.scripts.database.main as database
import admin_backend.scripts.brackets.main as brackets


with open('text.txt', 'r') as f:
    text = f.read()

new = brackets.edit_text_with_brackets(text)
print(new)