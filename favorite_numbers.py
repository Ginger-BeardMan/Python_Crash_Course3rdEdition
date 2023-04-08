
favorite_numbers = {
	'Joe': [5, 20, 30],
	'Mike': [25, 69, 72, 80],
	'Matt': [1, 2, 69, 5, 9],
	'Liz': [7],
	'Fen': [89, 7, 12]
	}

for person, numbers in favorite_numbers.items():
	if len(numbers) > 1:
		print(f"{person}'s favorite numbers are:")
		for number in numbers:
			print(f"{number}")
	else:
		print(f"{person}'s favorite number is:")
		for number in numbers:
			print(f"{number}")