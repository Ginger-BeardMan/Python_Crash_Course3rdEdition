from random import choice

lottery_numbers = [66, 93, 42, 5, 18, 99, 31, 2, 7, 26, 'A', 'G', 'S', 'K', 'Z']

roll = choice(lottery_numbers), choice(lottery_numbers), choice(lottery_numbers), choice(lottery_numbers)

winning_numbers = str(roll)

my_ticket = ('G', 'S', 2, 18)

print(winning_numbers)
print(my_ticket)

print(f'The winning lottery ticket is: {winning_numbers}! Congratulations!')

if my_ticket == winning_numbers:
	print('matching')
else:
	print('no match')