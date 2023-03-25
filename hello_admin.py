# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user. 

user_names = ['admin', 'belognalover225', 'johnsmith', 'BuTTmuNchEr69', 'Frank']

for name in user_names:
	if name == 'admin':
		print(f'Hello {name}, would you like to see a status report?')
	else:
		print(f'Hello {name}, thank you for logging in again. Welcome.')