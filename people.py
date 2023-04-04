people = {
	'person_1': {
		'first_name': 'John',
		'last_name': 'Smith',
		'age': 45,
		'city': 'San Jose'},
	'person_2': {
		'first_name': 'Sally',
		'last_name': 'McCarthy',
		'age': 66,
		'city': 'Boston'},
	'person_3': {
		'first_name': 'Arnold',
		'last_name': 'Shwarts',
		'age': 29,
		'city': 'Dallas'},
}

for person, person_info in people.items():
	full_name = f"{person_info['first_name']} {person_info['last_name']}"
	location = person_info['city']
	age = person_info['age']

	print(f'Your name is: {full_name.title()}')
	print(f'\nYou are located in {location.title()} and are {age} years old.')