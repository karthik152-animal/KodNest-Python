sentence = input()

cleaned = sentence.strip()
normalized = cleaned.lower().replace('.', '')

words = normalized.split()
slug = "-".join(words)

uppercase = normalized.upper()
python_position = normalized.find('python')

print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase}")
print(f"Python Position: {python_position}")