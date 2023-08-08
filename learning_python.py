from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text().rstrip()

print(contents)

learned_items = []

lines = contents.splitlines()

for line in lines:
	learned_items.append(line)
	#print(line)
	print(learned_items[-1])