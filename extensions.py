# improve/add to/change context many_users.py

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

users['dtownsend'] = {'first': 'Devin', 'last': 'townsend', 'location': 'united states'}

users['todinson'] = {'first': 'thor', 'last': 'odinson', 'location': 'asgard'}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	print(f"User's full name is {user_info['first'].title()} {user_info['last'].title()} and they are located in {user_info['location'].title()}")
	#full_name = f"{user_info['first']} {user_info['last']}"
	#location = user_info['location']

	#print(f"\tFull name: {full_name.title()}")
	#print(f"\tLocation: {location.title()}")