from pathlib import Path

filenames = ['dogs.txt', 'cats.txt', 'birds.txt']
for filename in filenames:
	path = Path(filename)
	try:
		contents = path.read_text()
		print(contents)
	except FileNotFoundError:
		print(f'File {path} could not be located at this time.')