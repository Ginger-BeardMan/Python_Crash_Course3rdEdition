from pathlib import Path
import json

def show_favorite_num(path):
	#write a seperate program that reads in this value and prints the message 'I know our favorite number! It's ____.'
	if path.exists():
		contents = path.read_text()
		favorite_number = json.loads(contents)
		return favorite_number
	else:
		return None

def get_favorite_num(path):
	#prompt for user's favorite number
	favorite_number = input('What is your favorite number? ')
	#use json.dumps() to store this number in a file
	contents = json.dumps(favorite_number)
	path.write_text(contents)
	return favorite_number

def get_num():
	path = Path('favorite_number.json')
	favorite_number = show_favorite_num(path)
	if favorite_number:
		print(f'I know your favorite number! It is {favorite_number}')
	else:
		favorite_number = get_favorite_num(path)
		print(f'We have now noted your favorite number of {favorite_number}')

get_num()