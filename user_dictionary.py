from pathlib import Path
import json

user_info = {}

def get_stored_user_info(path):
	'''get stored user information if available'''
	if path.exists():
		contents = path.read_text()
		user_info = json.loads(contents)
		return user_info
	else:
		return None

def get_new_user_info(path):
	'''add new user information if not already available'''
	user_info['username'] = input('What is your name? ')
	user_info['fav_color'] = input('What is your favorite color? ')
	user_info['country'] = input('What country do you live in? ')
	contents = json.dumps(user_info)
	path.write_text(contents)
	return user_info

def greet_user():
	'''greet the user by name.'''
	path = Path('user_info.json')
	user_info = get_stored_user_info(path)
	if user_info:
		print(f"Welcome back {user_info['username']}. We see you like {user_info['fav_color']} and live in {user_info['country']}.")
	else:
		user_info = get_new_user_info(path)
		print(f"We'll remember you when you come back, {user_info['username']} who likes {user_info['fav_color']} and lives in {user_info['country']}.")

greet_user()

#OBJECTIVES:

#ask for two more pieces of information

#store this information in a dictionary

#write this dictionary to a file using json.dumps() and read it back using json.loads()

#print a summary of user information