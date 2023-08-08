# cleaned the for loop up
from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text().rstrip()

print(contents)

lines = contents.splitlines()

for line in contents.splitlines():
	print(line.replace('Python', 'C'))

# cleaned the for loop up

path = Path('learning_python.txt')

contents = path.read_text().rstrip()

print(contents)

learned_items = []

for line in contents.splitlines():
	learned_items.append(line)
	#print(line)
	print(learned_items[-1])