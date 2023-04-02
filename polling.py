favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'rust',
	'phil': 'python',
}

take_poll = ['jen', 'mike', 'michele', 'lani', 'phil', 'johnny']

for name in favorite_languages:
	if name in take_poll:
		print(f'Thanks for taking the poll {name.title()}!')
	else:
		print(f'{name.title()}, please take the pole, it helps our friendship...')