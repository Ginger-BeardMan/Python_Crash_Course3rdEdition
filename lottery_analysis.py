from random import choice

character_choices = [66, 93, 42, 5, 18, 99, 31, 2, 7, 26, 'A', 'G', 'S', 'K', 'Z']

my_ticket = [66, 5, 42, 'K']

count = 0

while True:

	winning_numbers = []

	count += 1
	
	while len(winning_numbers) < 4:
		
		new_number = choice(character_choices)

		if new_number not in winning_numbers:
			winning_numbers.append(new_number)

	print(winning_numbers)

	if my_ticket == winning_numbers:
			
		print('Congratulations, you won one billion dollars!')
			
		print(f'It took {count} tries to get the winning number!')

		break
	
	print(count)