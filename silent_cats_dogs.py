from pathlib import Path

filenames = ['dogs.txt', 'cats.txt', 'birds.txt']
for filename in filenames:
	path = Path(filename)
	try:
		contents = path.read_text()
		print(contents)
	# changing the except to 'fail silently'
	except FileNotFoundError:
		pass