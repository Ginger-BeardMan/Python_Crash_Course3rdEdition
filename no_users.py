# Take hello_admin.py and add an if test 

user_names = ['admin', 'belognalover225', 'johnsmith', 'BuTTmuNchEr69', 'Frank']

if user_names:
	for name in user_names:	
		if name == 'admin':
			print(f'Hello {name}, would you like to see a status report?')
		else:
			print(f'Hello {name}, thank you for logging in again. Welcome.')
else:
	print('We need to find some users!')