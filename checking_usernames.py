# Create a program that simulates how websites ensure that everyone has a unique username

current_users = ['wayne', 'collin', 'ryan', 'drew', 'sara']

new_users = ['marshal', 'sheriff', 'Collin', 'champion', 'Wayne']

for user in new_users:
	if user.lower() in current_users:
		print('You will need to create a new username')
	else:
		print('Username is available')