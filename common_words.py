from pathlib import Path

def get_count(filename):
	try:
		contents = path.read_text(encoding='utf-8')
	except FileNotFoundError:
		pass
	else:
		words = contents.split()
		num_the = words.count('the')
		print(f'{path} has {num_the} times that "the" appear in the story.')
		true_num_the = words.count('The')
		print(f'{path} has {true_num_the} times that the word "The" appears in the story.')

filenames = ['Anthem.txt', 'War of the Worlds.txt']
for filename in filenames:
	path = Path(filename)
	get_count(path)